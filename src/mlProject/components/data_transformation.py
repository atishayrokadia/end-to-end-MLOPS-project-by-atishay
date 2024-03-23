import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd

from mlProject.config.configuration import ConfigerationManager
from mlProject.entity.config_entity import DatTransformationConfig

class DatTransformation:
    def __init__(self, config: DatTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"), index=False)
    
        logger.info("splitted data into training and testing")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

try:
    config = ConfigerationManager()
    data_transformation_config=config.get_data_transformation_config()
    data_transformation = DatTransformation(config=data_transformation_config)
    data_transformation.train_test_spliting()

except Exception as e:
    raise e