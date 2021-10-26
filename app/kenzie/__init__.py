import os 

import dotenv 

dotenv.load_dotenv() 

FILES_DIRECTORY = os.environ.get("FILES_DIRECTORY") 
if not os.path.isdir()