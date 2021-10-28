import os

import dotenv

from app.kenzie import ALLOWED_EXTENSIONS

dotenv.load_dotenv() 

from flask.helpers import safe_join
from werkzeug.datastructures import FileStorage
from datetime import datetime , timezone
from werkzeug.utils import secure_filename


FILES_DIRECTORY = os.environ.get("FILES_DIRECTORY") 
MAX_CONTENT_LENGTH=os.environ.get("MAX_CONTENT_LENGTH") 
ALLOWED_EXTENSIONS = os.environ.get("ALLOWED_EXTENSIONS")



def list_all_files():
    all_files = os.listdir(FILES_DIRECTORY) 
    return list(all_files) 

def get_path(filename:str):
    path = safe_join(FILES_DIRECTORY,filename)
    return path  

def list_files(path):
    files = os.listdir(path)
    return files

def get_extension(filename:str):
    extension = filename.split(".")[-1] 
    return extension


def check_if_empty_repo_exist():
    all_directories = os.listdir(FILES_DIRECTORY) 
    verify = [ ]

    for directories in all_directories:
        verify.append(os.path.isfile(directories))

    return all(verify)   


def save_image(file: FileStorage):
    file_extension = file.filename.split(".")[-1]
    filename = str(datetime.now(timezone.utc))[:26] 
    filename = secure_filename(filename) 
    filename = f'{filename}.{file_extension}'
    path = safe_join(FILES_DIRECTORY, f'{file_extension}/{filename}')
    
    file.save(path)
    
    return filename

def verify_extension(file:FileStorage):
    file_extension = file.filename.split(".")[-1]
    return file_extension


def download_zip_files(extension):   
    os.system(f'zip -r /tmp/{extension}.zip images/{extension}')
    #os.system(f'zip -r /tmp/{extension}.zip images/{extension}')
    return {"message": "arquivo zip na pasta temp"}
    
     
def content_length():
    return MAX_CONTENT_LENGTH
    
    
def allowed_extensions():
    extensoes_permitidas = ALLOWED_EXTENSIONS.split('.')
    return list(extensoes_permitidas)