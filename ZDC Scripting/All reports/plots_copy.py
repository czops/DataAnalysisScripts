import numpy as np
import pandas as pd
import csv
from datetime import datetime
import datetime as dt
import matplotlib.pyplot as pp

#all data including empty lines
CleanedData = pd.read_csv('cleanedData.csv')

#convert all TimeIns to Datetime format
CleanedData['TimeIn'] = CleanedData['TimeIn'].str[:11]
print(CleanedData['TimeIn'])

rackCounts = CleanedData[(CleanedData['TimeIn'], CleanedData['Process' != 'EmptyLine'])]
rackCounts.set_index('TimeIn', inplace=True)
print(rackCounts)

#rackCounts.groupby(rackCounts.index.date).count()
#print(rackCounts)
print(CleanedData['TimeIn'].value_counts())

#index by date and process
rackCount = CleanedData.set_index(['TimeIn', 'Process'])
#print(rackCount)
#rackCount

#groupings
CleanedData_only26D = CleanedData[(CleanedData['Process'] == 'US26D')]
CleanedData_onlyNickel = CleanedData[(CleanedData['Process'] == 'NickelOnly')]
CleanedData_onlyBrightCopper = CleanedData[(CleanedData['Process'] == 'BrightCopper')]
CleanedData_only10BCopper = CleanedData[(CleanedData['Process'] == '10B Copper')]


#Issues.plot(x="TimeIn", y="Process_Time")
#CleanedData2.plot(x="TimeIn", y="Process_Time")
#CleanedData2.hist()

rackCounts.plot(x="TimeIn", y="Process")

#print(CleanedData2.describe())
#pp.hist(CleanedData2['Process_Time'], bins=20)
#pp.hist(Issues_withoutEmptyLine['Process_Time'], bins=20)
#pp.hist(CleanedData['TimeIn'], bins=30)

pp.show()
