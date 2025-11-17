import os
import urllib.request as request
from src.mlops_pipeline import logger
import zipfile
from src.mlops_pipeline.entity.config_entity import (DataIngestionconfig)


#DataIngestion Component

class DataIngestion:
    def __init__(self,config:DataIngestionconfig):
        self.config=config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url= self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info \n{headers}")
        else:
            logger.info(f"Rile already exists")
            
            
    def extract_zip_file(self):
        """ 
        zip_file_path:str
        Extracts the zip file into the data directory
        Function returne None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        