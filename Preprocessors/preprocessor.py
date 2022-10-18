import pandas as pd
import os
import numpy as np

# Where the data is stored Z:\REPO\Code\Python\DataStoryteller\DataStorage\PickleJar
root = 'Z:/REPO/Code/Python/DataStoryteller'
path = 'DataStorage/PickleJar'
file = 'data_frame.pickle'
PATH_TO = os.path.join(root, path, file)
# All columns needed
COLS_TO_USE = ['Trigger Index', 'Trigger Name',
               'Trigger Value', 'Message', 'Alarm Time (UTC)']
numericCols = np.NaN
fillMissing = False


# Preprocess data for storage in pickle format
def dataTidy(df):
    """Constants"""

    # Select columns
    df = df.loc[:, COLS_TO_USE]
    shallowDf = df.copy(deep=False)  # Reflects changes to original

    # convert time format to string
    shallowDf['Alarm Time (UTC)'].str.rsplit(' ', expand=True)
    #shallowDf = shallowDf.iloc[:, 1].to_datetime("%H:%M:%S").dt.time

    shallowDf = shallowDf.assign(date=shallowDf.iloc[:, 0], time=shallowDf.iloc[:, 1])  # Create and assign to new column


    # assign shift - S1 = '07:01:00' - '19:00:00', S2 = '19:01:00' - '07:00:00'
    # create new column
    shallowDf = shallowDf.assign(shift='')
    # assign values
    shallowDf.loc[shallowDf['time'] >= '07:00:00', 'shift'] = 'S1'
    shallowDf.loc[shallowDf['time'] < '07:00:00', 'shift'] = 'S2'
    shallowDf.loc[shallowDf['time'] >= '19:00:00', 'shift'] = 'S2'

    shallowDf

    # remove column
    # df.drop['Alarm Time (UTC)']

    #
    # for n in numericCols:
    #     if (fillMissing):
    #         pd.to_numeric(df[n], errors='coerce')
    #     else:
    #         pd.to_numeric(df[n])
    # Index ID
    # if not shallowDf['id']:
    #     shallowDf.index = [lambda x: x in range(1, len(df.values) + 1)]
    #     shallowDf.index.name = 'id'
    # # Set index and drop duplicate
    # shallowDf.set_index('id', drop=True, inplace=True)
    #
    # Save data in data store - using surrealisation
    shallowDf.to_pickle(PATH_TO)
    # print(shallowDf)
