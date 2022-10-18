import pandas as pd
import os

# Connection type
conn = 'csv'
# Where the data lives
root = '../'
path = 'DataStorage/Datasets/BorgWarner/'
file = '2022_09_30_07_28_28-DESKTOP-I3FQ91U-ALARM.csv'
CSV_PATH = os.path.join('Z:/REPO/Code/Python/DataStoryteller/DataStorage/Datasets/BorgWarner/2022_09_30_07_28_28-DESKTOP-I3FQ91U-ALARM.csv')
records = 5
# Connections
def connect():
    # Connection type
    if (conn == 'csv'):
        df = pd.read_csv(CSV_PATH, nrows=records)
        return df
    elif (conn == 'msSql'):
        df = pd.read_csv(CSV_PATH, nrows=records)
        return df
    elif (conn == 'postgre'):
        df = pd.read_csv(CSV_PATH, nrows=records)
        return df
    elif (conn == 'oracle'):
        df = pd.read_csv(CSV_PATH, nrows=records)
        return df
    elif (conn == 'roc'):
        df = pd.read_csv(CSV_PATH, nrows=records)
        return df
    else:
        print('No connection type selected')
