import numpy as np
import pandas as pd

from datetime import datetime
import datetime as dt
import matplotlib.pyplot as pp

pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 100)

#all data including empty lines
CleanedData = pd.read_csv('cleanedData.csv')
#only faults 
Issues = pd.read_csv('Issues.csv')
#totalrackcount
RackCount = pd.read_csv('CleanedData2.csv')


#convert all TimeIns to Datetime format
#def convertTimeIns():
CleanedData['TimeIn'] = CleanedData['TimeIn'].str[:11]
print(CleanedData['TimeIn'])
print(CleanedData['TimeIn'].value_counts())

print(CleanedData.groupby('TimeIn')['Process'].value_counts())
#print(CleanedData.groupby('TimeIn')['Process'].apply(lambda x: x.value_counts().head(1)))

#total_counts = CleanedData['TimeIn'].str[:11].to_list()

#date_set = CleanedData['TimeIn'].value_counts().set()

print(type(CleanedData['TimeIn'].value_counts()))
countsperday = CleanedData['TimeIn'].value_counts()


#NOT WORKING
#index by date and process
rackCount = CleanedData.set_index(['TimeIn', 'Process'])
print(rackCount)




#print(dateList)
#print(date_set)

#Set up dataframes for plotting
CleanedData_withoutEmptyLine = CleanedData[(CleanedData['Process'] != 'EmptyLine')]
Issues_withoutEmptyLine = Issues[(Issues['Process'] != 'EmptyLine')]

#groupings by recipe
#create numpyArrays
CleanedData_only26D = CleanedData[(CleanedData['Process'] == 'US26D')]
US26D = CleanedData_only26D.loc[:, 'TimeIn']
print(US26D)
print("series of US26D flight bars run")


CleanedData_only26D['TimeIn'] = CleanedData_only26D['TimeIn'].str[:11]
CleanedData_only26D['TimeIn'] = pd.to_datetime(CleanedData_only26D['TimeIn'], format = None)
CleanedData_only26D['TimeIn'] = CleanedData_only26D['TimeIn'].sort_values(ascending = True)
US26D_counts = CleanedData_only26D['TimeIn'].value_counts()

print(US26D_counts)
US26D_counts_list = US26D_counts.tolist()
print("++++++++++++++++++++++++++++++")

#US26D_counts.sort_values(ascending = True)

print(US26D_counts)
print("counts series of US26D flight bars run")

CleanedData_onlyNickel = CleanedData[(CleanedData['Process'] == 'NickelOnly')]
CleanedData_onlyNickel['TimeIn'] = CleanedData_onlyNickel['TimeIn'].str[:11]
CleanedData_onlyNickel['TimeIn'] = pd.to_datetime(CleanedData_onlyNickel['TimeIn'], format = None)
CleanedData_onlyNickel['TimeIn'] = CleanedData_onlyNickel['TimeIn'].sort_values(ascending = True)
Nickel_counts = CleanedData_onlyNickel['TimeIn'].value_counts()

CleanedData_onlyBrightCopper = CleanedData[(CleanedData['Process'] == 'BrightCopper')]
CleanedData_only10BCopper = CleanedData[(CleanedData['Process'] == '10B Copper')]

#Need to change the TimeIn column to Datetime format
CleanedData_withoutEmptyLine.groupby(['TimeIn'])


   
#count the racks per day

#ProdDataSelection = ProdData2[(ProdData2['Process_Time'] > 0) & (ProdData2.Process_Time < 6)]

#Issues.plot(x="TimeIn", y="Process_Time")
#CleanedData2.plot(x="TimeIn", y="Process_Time")
#CleanedData.plot(x="TimeIn", y="Process_Time")
#CleanedData2.hist()
#rackCount.plot(x="TimeIn", y="Process")

#US26D_counts.hist()
US26D_counts.plot()
Nickel_counts.plot()


#pp.plot(US26D_counts)
#pp.plot(CleanedData_only26D['TimeIn'], CleanedData_only26D['TimeIn'].value_counts())

#print(CleanedData2.describe())
#pp.hist(CleanedData2['Process_Time'], bins=20)
#pp.hist(Issues_withoutEmptyLine['Process_Time'], bins=20)
#pp.hist(CleanedData['TimeIn'], bins=30)

pp.show()
