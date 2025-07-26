import os
import certifi
import numpy as np
import pandas as pd
import sys
import json
from datetime import datetime
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
from networkSecurity.exception.exception import NetworkSecurityExcepion
from networkSecurity.logging.logger import logger
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print("MongoDB URL:", MONGO_DB_URL)
ca=certifi.where()# Ensure secure connection with CA certificates

class NetworkDataExtract():

    def __init__(self):
        try:
            pass
        except Exception as e:
            logger.error(f"Error in NetworkDataExtract initialization: {e}")
            raise NetworkSecurityExcepion(e, sys) 

    def csv_to_json(self,file_path:str):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            recorsds=list(json.loads(data.T.to_json()).values())
            return recorsds
        except Exception as e:
            logger.error(f"Error in csv_to_json method: {e}")
            raise NetworkSecurityExcepion(e, sys)

    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.db=self.mongo_client[self.database]
            self.collection=self.db[self.collection]
            self.collection.insert_many(self.records)
            logger.info(f"Data inserted successfully into {self.database}.{self.collection}")
            return len(self.records)
        except Exception as e:
            logger.error(f"Error in insert_data_to_mongodb method: {e}")
            raise NetworkSecurityExcepion(e, sys)
        
if __name__ == "__main__":
    File_Path='Network_Data/phisingData.csv'
    Database='NetworkSecurity'
    Collection='phishing_data'
    try:
        networkobj = NetworkDataExtract()
        records = networkobj.csv_to_json(File_Path)
        print(records)
        no_of_records = networkobj.insert_data_to_mongodb(records, Database, Collection)
        logger.info(f"Total records inserted: {no_of_records}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise NetworkSecurityExcepion(e, sys)