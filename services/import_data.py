import os
import logging
import pandas as pd


covid_url = os.getenv('COVID_DATA_URL')

def import_data(dtype='confirmed'):
    time_series_path = 'time_series_19-covid-'
    extension = '.csv'
    if dtype.lower() == 'confirmed':
        fname = time_series_path + 'Confirmed' + extension
    elif dtype.lower() == 'deaths':
        fname = time_series_path + 'Deaths' + extension
    elif dtype.lower() == 'recovered':
        fname = time_series_path + 'Recovered' + extension
    else:
        logging.error("dtype not recognised.")
        ValueError("dtype not recognised.")
    
    url = covid_url + '/' + fname

    df = pd.read_csv(url)

    # save imported data to local file
    save_path = '/app/data/' + fname
    df.to_csv(save_path)
    
    