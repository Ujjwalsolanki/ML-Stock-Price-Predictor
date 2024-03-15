import os
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr

from plotly.offline import iplot
import plotly as ply
import plotly.tools as tls
import cufflinks as cf
# Below code is needed for plotly offline version
ply.offline.init_notebook_mode(connected = True)
cf.go_offline()

import plotly.io as pio
pio.renderers.default = "vscode"

import yfinance as yf
yf.pdr_override()

from logger import logging

class DataIngestion():
    def __init__(self):
        self.start = dt.datetime(2015,1,1)
        self.end = dt.datetime.now()
        self.share_name = 'TSLA'
        self.path = os.path.join('training_files/')

    def initiate_data_ingestion(self):
        try:
            df = pdr.get_data_yahoo(self.share_name, self.start, self.end)
            logging.info("got data")
            
            df.to_csv(self.path + 'data.csv')
        except Exception as e:
            logging.exception(e)
            raise e

