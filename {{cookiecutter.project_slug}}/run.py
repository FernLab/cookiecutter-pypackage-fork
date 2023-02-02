"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

import os
import uvicorn
from dotenv import load_dotenv

if __name__ == "__main__":
    data_dir_in = None
    try:
        application_scope = os.environ['API_SERVER_SCOPE']
        if application_scope == 'DEPLOYMENT':
            try:
                PORT = int(os.environ['PORT'])
                if not PORT:
                    raise EnvironmentError('<PORT> environment needs to be set.')
            except:
                raise EnvironmentError('Check .env file to see if you set <DATA_DIR> environment.')
            try:
                data_dir = os.environ['DATA_DIR']
                if not data_dir:
                    raise EnvironmentError('<DATA_DIR> environment needs to be set.')
            except:
                raise EnvironmentError('Check .env file to see if you set <DATA_DIR> environment.')

        # In debug mode 
        elif application_scope == 'DEVELOPMENT':
                try:
                    PORT = int(os.getenv('PORT'))
                    if not PORT:
                        raise EnvironmentError('<PORT> environment needs to be set.')
                except:
                    raise EnvironmentError('Check .env file to see if you set <DATA_DIR> environment.')
                data_dir = os.path.join(os.getcwd(), 'data_dir')
        else:
           raise ValueError(f'Unsupported value for the <API_SERVER_SCOPE> environment => {application_scope}')
        
    except:
        # In case of using python run.py
        try:
            load_dotenv()
            application_scope = os.getenv('API_SERVER_SCOPE')

            if application_scope == 'DEVELOPMENT':
                try:
                    PORT = int(os.getenv('PORT'))
                    if not PORT:
                        raise EnvironmentError('<PORT> environment needs to be set.')
                except:
                    raise EnvironmentError('Check .env file to see if you set <DATA_DIR> environment.')
                data_dir = os.path.join(os.getcwd(), 'data_dir')
            else:
                raise ValueError(f'Unsupported value for the <API_SERVER_SCOPE> environment => {application_scope}')
        except:
            raise EnvironmentError('Check .env file to see if you set <API_SERVER_SCOPE> environment.')
    
    os.environ['DATA_DIR'] = data_dir

    print('\n')
    print('~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~')
    print('~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~')
    print('Application is up and running successfully.')
    print('~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~')
    print('~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~\n')
    print(f'Application Scope => {application_scope}')
    print(f'Running on Port => {PORT}')
    
    if application_scope == 'DEPLOYMENT':
        print('Volume Link =>')
        print(f'{data_dir}:/home/data/data_dir')

    else:
        print(f'Data DIR => {data_dir}')

    print('\n~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~')
    print('~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~\n')

    uvicorn.run("fastapi_boilerplate.create_app:app", host='0.0.0.0', port=PORT, reload=True)
