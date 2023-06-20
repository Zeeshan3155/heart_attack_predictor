from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

import sys 
import pandas as pd
import numpy as np
import os
from dataclasses import dataclass


from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw_data.csv')

class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Reading data")
            df = pd.read_csv('.\data\heart.csv')

            X = df.drop(columns=['output'])
            y = df['output']
            
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=0)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Data ingestion complete")

            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path,self.ingestion_config.raw_data_path)
            
        except Exception as e:
            raise CustomException(e,sys)