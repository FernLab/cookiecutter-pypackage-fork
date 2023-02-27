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
    except:
        # Here is for
        # python run.py
        load_dotenv()
        try:
             application_scope = os.getenv('API_SERVER_SCOPE')
             
        except:
            raise IOError(f'Undefined SCOPE for the service. Environment <API_SERVER_SCOPE> should be set.')

    if application_scope not in ['DEPLOYMENT', 'DEVELOPMENT']:
        raise ValueError(f'Unsupported "{application_scope}" for the <API_SERVER_SCOPE> environment.')
    
    # Here is for
    # docker-compose up
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

    # Here is for
    # IDE debugger
    elif application_scope == 'DEVELOPMENT':
            try:
                PORT = int(os.getenv('PORT'))
                if not PORT:
                    raise EnvironmentError('<PORT> environment needs to be set.')
            except:
                raise EnvironmentError('Check .env file to see if you set <DATA_DIR> environment.')
            data_dir = os.path.join(os.getcwd(), 'data_dir')
        
    # except:
    #     # In case of using python run.py
    #     try:
    #         load_dotenv()
    #         application_scope = os.getenv('API_SERVER_SCOPE')

    #         if application_scope == 'DEVELOPMENT':
    #             try:
    #                 PORT = int(os.getenv('PORT'))
    #                 if not PORT:
    #                     raise EnvironmentError('<PORT> environment needs to be set.')
    #             except:
    #                 raise EnvironmentError('Check .env file to see if you set <DATA_DIR> environment.')
    #             data_dir = os.path.join(os.getcwd(), 'data_dir')
    #         else:
    #             raise ValueError(f'Unsupported value for the <API_SERVER_SCOPE> environment => {application_scope}')
    #     except:
    #         raise EnvironmentError('Check .env file to see if you set <API_SERVER_SCOPE> environment.')
    
    os.environ['DATA_DIR'] = data_dir

    print('\n')
    print('~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~')
    print('~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~')
    print('...::: Trying to run the application :::...')
    print('~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~\n')
    print(f'Scope => {application_scope}')
    print(f'Port => {PORT}')
    
    if application_scope == 'DEPLOYMENT':
        print('Volume Link =>')
        print(f'{data_dir}:/home/data/data_dir')

    else:
        print(f'Data DIR => {data_dir}')

    print('\n~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~')
    print('~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~\n')

    uvicorn.run("{{ cookiecutter.project_slug }}.create_app:app", host='0.0.0.0', port=PORT, reload=True)
