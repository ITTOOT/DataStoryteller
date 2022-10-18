import pandas as pd
import os

# TO DO - ADD CALLBACKS AND FORM ELEMENTS TO HANDLE USER OPERATIONS

# Data loading
root = '..'
path = 'DataStorage/Datasets/PickleJar'
file = 'data_frame.pickle'
df = os.path.join(root, path, file)
carbonCopy = True
# Make a copy to work on
if (carbonCopy):
    copyDf = df.copy(deep=True)  # Independent of original
else:
    copyDf = df.copy(deep=False) # Reflects changes to original

# ANALYSIS - goes in separate file
filterCol = 'time'
filterVal = '21:58:16'
shiftVal = 'day'
cols = ''
# Filter column, filter value
copyDf.loc[copyDf[filterCol] == filterVal, : ] # Infers labels from expression, gets all columns with " : "

# Order by date
sortVal = 'Alarm Time (UTC)'
# USE ARROW TO DECIDE DIRECTION
copyDf[sortVal].sort_values().head()
copyDf[sortVal].sort_values().tail()

# Top/bottom "n"
n = 10
copyDf.head(n)
copyDf.tail(n)

# Groups
# Get values for shift
toDash = []
groupVal = 'shift'
aggregator = []
aggregator[0] = 'time'
grouped = copyDf.groupby(groupVal)
series = copyDf['medium']

# Aggregates - check for relations & causality
for name, groupDf in grouped:
    toDash[0] = name
    toDash[1] = groupDf
    # Analyse groups
    minVal = groupDf[aggregator[0]].min()
    maxVal = groupDf[aggregator[0]].max()

# Number of occurrences
# Count the recurrence values for each entry in a series
countedVals = series.value_counts()
minVal = countedVals.min()
maxVal = countedVals.max()

# Strings
searchCol = 'date'
pos = 3
length = 0 # default
searchVal = '5'
subString = '19A'
# Match position value to search value
copyDf[copyDf[searchCol].str[pos] == searchVal]
# Only values greater than length
copyDf[copyDf[searchCol].str.len() > length]
# Contains sub-string
copyDf[copyDf[searchCol].str.contains(subString)]

# Rename columns
nameFrom = 'Alarm Time (UTC)'
nameTo = 'Alarm Time'
copyDf.rename(columns={nameFrom : nameTo}, inplace=True)

# Lambda
searchCol = []
searchVals = []
resultDf = list(filter(lambda x: x[searchCol[0]] == searchVals[0] and
                               x[searchCol[1]] == searchVals[1]), copyDf)


# Get unique values
copyDf = df[filterCol] # Filter column
pd.unique(copyDf) # Find unique values in column
