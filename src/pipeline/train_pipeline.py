import os
print(os.getcwd())
import sys
sys.path.append(os.getcwd())

from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataTransformationConfig

from src.components.data_transfermation import DataTransformation
from src.components.data_transfermation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

class train_pipeline:
    def __init__(self):
        pass

    def model_training(self):
        try:
            logging.info("Data Ingession Strated")
            obj=DataIngestion()
            train_data,test_data=obj.initiate_data_ingestion()
            logging.info("Data Ingession Completed")

            logging.info("Data Transfermation Started ")
            data_transformation=DataTransformation()
            train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
            logging.info("Data Transfermation Completed ")

            logging.info("Model Training Started ")
            modeltrainer=ModelTrainer()
            print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
            logging.info("Model Training Completed")

        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    model=train_pipeline()
    model.model_training()