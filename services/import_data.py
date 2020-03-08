import os
import logging
import pandas as pd


covid_url = os.getenv('COVID_DATA_URL')
data_path = '/app/data/'
extension = '.csv'


def import_data(dtype='confirmed'):
    # construct file url
    time_series_path = 'time_series_19-covid-'
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

    logging.info(f"READING data from {url}")

    df = pd.read_csv(url)

    # replace American date format, lowercase other column names
    df.columns = [
        pd.to_datetime(col, format="%m/%d/%y").date()
        if col in df.filter(regex="[0-9]+/[0-9]+/[0-9]+")
        else col.lower()
        for col in df.columns
    ]

    # save imported data to local file
    save_path = data_path + dtype.lower() + extension
    df.to_csv(save_path, index=False)

    logging.info(f"SAVED data to file {save_path}")


def read_data(dtype='confirmed'):
    file_path = data_path + dtype.lower() + extension

    df = pd.read_csv(file_path)

    return df


def get_date_col_names(df):
    """
    Return the DataFrame column names that have the yyyy-mm-dd date format.
    """
    return df.filter(regex="[0-9]{4}-[0-9]{2}-[0-9]{2}").columns