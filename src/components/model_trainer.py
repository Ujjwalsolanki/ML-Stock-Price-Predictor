import os
from logger import logging
import pandas as pd
from pathlib import Path

from src.utils.common import FileOperations


class Model_Trainer:
    def __init__(self):
        self.data_path = Path('training_files/data.csv')
        self.model_path = Path('artifacts/models/')
    
    def initiate_model_training(self):
        try:
            data = pd.read_csv(self.data_path)

            df1 = pd.DataFrame()
            df1['y'] = data.Close
            df1['ds'] = pd.to_datetime(data['Date'])
            df1

            from prophet import Prophet
            model = Prophet()
            model.fit(df1)
            file_op = FileOperations()
            file_op.save_model(model, self.model_path, "model.pkl")

            model2 = file_op.load_model("model.pkl")

            future = model2.make_future_dataframe(periods = 1,freq='D')
            forecast = model2.predict(future)
            print(forecast.tail())
            logging.info(pd.DataFrame(forecast.tail()))

        except Exception as e:
            logging.exception(e)
            raise e



    