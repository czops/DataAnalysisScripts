from sqlite3 import Time
import numpy as np
import pandas as pd

from datetime import datetime
import datetime as dt
import matplotlib.pyplot as pp

#all data including empty lines
CleanedData = pd.read_csv('cleanedData.csv')
#only faults 
Issues = pd.read_csv('Issues.csv')
#totalrackcount
RackCount = pd.read_csv('CleanedData2.csv')

#to get rack counts
def TimesToDates():
    #convert all TimeIns to Datetime format
    CleanedData['TimeIn'] = CleanedData['TimeIn'].str[:11]

    print('LINE 21')
    print(CleanedData.groupby('TimeIn')['Process'].value_counts())
    groupedData = CleanedData.groupby('TimeIn')['Process'].value_counts()
    
    print('LINE 25')
    print(groupedData)

    #this is incorrect... pulling the values for dates instead of rack numbers

    #dates = CleanedData.loc[CleanedData['TimeIn']].values
    #Chrome = CleanedData.loc[CleanedData['Process'] == 'US26D', 'TimeIn'].values
    #print('LINE 32')
    #print(Chrome)
    #Nickel = CleanedData.loc[CleanedData['Process'] == 'NickelOnly', 'TimeIn'].values
    #USTenBcopper = CleanedData.loc[CleanedData['Process'] == '10B Copper', 'TimeIn'].values
    #BrightCopper = CleanedData.loc[CleanedData['Process'] == 'BrightCopper', 'TimeIn'].values

    groupedData.to_csv('RackCounts.csv')
    pp.plot(groupedData, c = 'b', label = 'Rack Counts')




#run functions in correct order
TimesToDates()
