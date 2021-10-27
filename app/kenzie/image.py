import os
import dotenv 
from flask.helpers import safe_join

dotenv.load_dotenv() 

FILES_DIRECTORY = os.environ.get("FILES_DIRECTORY") 

def list_all_directories():
    all_directories = os.listdir(FILES_DIRECTORY) 
    return list(all_directories) 


def check_if_empty_repo_exist():
    all_directories = os.listdir(FILES_DIRECTORY) 
    verify = [ ]

    for directories in all_directories:
        verify.append(os.path.isfile(directories))

    return all(verify)   

def list_all_images():
    _,_,images_list =list(os.walk(FILES_DIRECTORY))[0]
    return images_list

    
   
def get_path(filename:str):
    path = safe_join(FILES_DIRECTORY,filename)