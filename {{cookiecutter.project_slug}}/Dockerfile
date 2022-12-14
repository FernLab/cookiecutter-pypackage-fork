# ref https://github.com/tebeka/pythonwise/blob/master/docker-miniconda/Dockerfile
FROM python:3.10-slim-buster

# System packages
RUN apt-get update -y && \
    echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get install -y -q dialog apt-utils && \
    apt-get install libudunits2-dev build-essential bash-completion automake -y && \
    apt-get install cmake zlib1g-dev libpng-dev libjpeg-dev -y  && \
    apt-get install wget vim zip unzip curl git git-lfs jq apt-rdepends -y && \
    apt-get install strace bzip2 cron make gcc -y && git-lfs install

# Install mambaforge
RUN curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
RUN bash Mambaforge-$(uname)-$(uname -m).sh -b -p /mambaforge
RUN rm Mambaforge-$(uname)-$(uname -m).sh
ENV PATH=/mambaforge/bin:${PATH}

# Python packages from conda
RUN mamba install -y python=3.9
RUN mamba install -y pip
RUN mamba init bash

# copy some needed stuff to /root
COPY /tests/CI_docker/context/environment_{{ cookiecutter.project_slug }}.yml /root/
RUN mamba env create -f /root/environment_{{ cookiecutter.project_slug }}.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "{{ cookiecutter.project_slug }}", "/bin/bash", "-c"]

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Install {{ cookiecutter.project_slug }}
ADD . /{{ cookiecutter.project_slug }}/

RUN pip install -e /{{ cookiecutter.project_slug }}/

# Copy local code to the container image.
ENV APP_HOME /{{ cookiecutter.project_slug }}/
WORKDIR $APP_HOME

# Make sure the environment is activated:
RUN echo "Make sure FastAPI is installed:"
RUN python -c "import fastapi"
RUN echo "Make sure uvicorn is installed:"
RUN python -c "import uvicorn"
