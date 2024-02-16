import os
from waitress import serve
from ApexAzurePromo.wsgi import application

this_files_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(this_files_dir)

if __name__ == '__main__':
    serve(application, host = 'localhost', port = '8001')
