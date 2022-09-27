import numpy as np
import pandas as pd
import csv
from datetime import datetime
import datetime as dt
import matplotlib.pyplot as pp

#all data including empty lines
CleanedData = pd.read_csv('cleanedData.csv')
#only faults 
Issues = pd.read_csv('Issues.csv')
CleanedData2 = pd.read_csv('CleanedData2.csv')

#convert all TimeIns to Datetime format
CleanedData['TimeIn'] = CleanedData['TimeIn'].str[:11]
print(CleanedData['TimeIn'])

print(CleanedData['TimeIn'].value_counts())
print(type(CleanedData['TimeIn'].value_counts()))

#dateList = CleanedData['TimeIn'].to_list()
#dateList = [d[0:11] for d in dateList]
#date_set = set(dateList)

#print(dateList)
#print(date_set)

CleanedData_withoutEmptyLine = CleanedData[(CleanedData['Process'] != 'EmptyLine')]
Issues_withoutEmptyLine = Issues[(Issues['Process'] != 'EmptyLine')]

#groupings
CleanedData_only26D = CleanedData[(CleanedData['Process'] == 'US26D')]
CleanedData_onlyNickel = CleanedData[(CleanedData['Process'] == 'NickelOnly')]
CleanedData_onlyBrightCopper = CleanedData[(CleanedData['Process'] == 'BrightCopper')]
CleanedData_only10BCopper = CleanedData[(CleanedData['Process'] == '10B Copper')]

#Need to change the TimeIn column to Datetime format
CleanedData_withoutEmptyLine.groupby(['TimeIn'])



#count the racks per day




#ProdDataSelection = ProdData2[(ProdData2['Process_Time'] > 0) & (ProdData2.Process_Time < 6)]

#Issues.plot(x="TimeIn", y="Process_Time")
#CleanedData2.plot(x="TimeIn", y="Process_Time")
#CleanedData2.hist()

print(CleanedData2.describe())
#pp.hist(CleanedData2['Process_Time'], bins=20)
#pp.hist(Issues_withoutEmptyLine['Process_Time'], bins=20)
pp.hist(CleanedData['TimeIn'], bins=30)

pp.show()
