import os

import dotenv

dotenv.load_dotenv() 

from flask.helpers import safe_join
from werkzeug.datastructures import FileStorage
from datetime import datetime , timezone
from werkzeug.utils import secure_filename


FILES_DIRECTORY = os.environ.get("FILES_DIRECTORY") 


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


def list_all_images_files():
    files_list = os.listdir(FILES_DIRECTORY)
    return files_list



def check_if_empty_repo_exist():
    all_directories = os.listdir(FILES_DIRECTORY) 
    verify = [ ]

    for directories in all_directories:
        verify.append(os.path.isfile(directories))

    return all(verify)   








def png_path(filename:str):
    path = safe_join(f'{FILES_DIRECTORY}/png',filename)
    return path 

def save_image(file: FileStorage):
    file_extension = file.filename.split(".")[-1]
    filename = str(datetime.now(timezone.utc))[:26] 
    filename = secure_filename(filename) 
    filename = f'{filename}.{file_extension}'
    path = safe_join(FILES_DIRECTORY, filename)
    
    file.save(path)
    return filename


def dowload_zip_dir(path):
    comando = f'{path} touch nicole.txt'
    os.system(comando)
    
    