# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import numpy as np
import Readers.comms as com
import Preprocessors.preprocessor as pre

# Connect & retrieve file
dataframe = com.connect()



#RUN
# Pre-process data
pre.dataTidy(dataframe)
