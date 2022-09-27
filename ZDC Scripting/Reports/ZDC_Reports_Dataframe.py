import glob

import numpy as np
import pandas as pd

import csv
from datetime import datetime
import datetime as dt


headers = ['FileName','Process','Workbar', 'TimeIn', 'TimeOut', 'ProcessTime', 'Part Number 1', 'Qty 1', 'Part Number 2', 'Qty 2','Part Number 3', 'Qty 3', 'Part Number 4', 'Qty 4', 'Part Number 5', 'Qty 5']

#add 20 ~ steps to the headers
step_numbers = []
for i in range(0,25):
    step_numbers.append(i)

for i in step_numbers:
    headers.append(i)


ProdData = pd.read_csv('mycsvfile2.csv') # names = headers)

ProdData.replace(' ', np.nan, inplace=True)

print(ProdData['TimeOut'])

#remove NaNs
print('================')

ProdData2 = ProdData.dropna(subset=['TimeOut'])

def correctingDates():
    date_list = []
    datetime_list = []
    time_in = []
    time_out = []

    datesList = ProdData['FileName']

    counter = 0
    for date in datesList:
        
        #date portion
        yyyymmdd = date[0:8]
        print(type(yyyymmdd))
        print(yyyymmdd)

        #time in portion
        sep = '_'
        time_string = date.split(sep, 1)[1]
        if len(time_string) > 6:
            time_string = time_string[0:2] + ":" + time_string[2:7]
        else:
            time_string = time_string[0] + ":" + time_string[1:7]
        
        new_DateTime = yyyymmdd + ' ' + time_string

        print(type(time_string))
        print(time_string)
       

        date_object = datetime.strptime(yyyymmdd, '%Y%m%d').strftime('%m/%d/%Y')
        date_object2 = datetime.strptime(new_DateTime, '%Y%m%d %H:%M %p').strftime('%m/%d/%Y %H:%M')
        print(date_object)
        print(date_object2)

        #need to get the end time as parts hit 'Station 1 Unload Shuttle'
        #find row being worked on
        row = ProdData.iloc[counter]
        print('=========================================')
        print(row)
        print(type(row))

        time_out = ''

        #date_time_obj = datetime.strptime(date, '%y/%m/%d %H:%M')
        date_list.append(date_object)
        datetime_list.append(date_object2)

        counter = counter + 1

    ProdData['Date'] = date_list
    ProdData['DateTimeIn'] = datetime_list
    #ProdData['Time'] = time_list


    print(datesList)

def find_InOut():
    
    #this will not work without removing rows with no TimeOut or with spaces (weird sometimes this happens where the program puts " " instead of blank or NaN)
    
    print(ProdData2['TimeIn'])
    ProdData2['TimeIn'] = pd.to_datetime(ProdData2['TimeIn'], format = '%Y/%m/%d %H:%M')
    print(ProdData2['TimeIn'])
    print(ProdData2['TimeOut'])
    ProdData2['TimeOut'] = pd.to_datetime(ProdData2['TimeOut'], format = '%Y/%m/%d %H:%M')
    print(ProdData2['TimeOut'])
    ColTimeIn = ProdData2['TimeIn']
    ColTimeOut = ProdData2['TimeOut']


    #datetime.strptime(yyyymmdd, '%Y%m%d %H:%M').strftime('%m/%d/%Y')
    ProdData2['Process_Time'] = (ColTimeOut - ColTimeIn)
    ProdData2['Process_Time'] = pd.to_timedelta(ProdData2['Process_Time']).dt.total_seconds() / 3600

    

    #ProdData2 = ProdData2.drop(ProdData2['Process Time'] > 8)

#correctingDates()
find_InOut()

#DF for plotting recipe times (either reference works - brackets or dot operator)
ProdDataSelection = ProdData2[(ProdData2['Process_Time'] > 0) & (ProdData2.Process_Time < 6)]
#DF for fault tracking
ProdDataFaults = ProdData2[(ProdData2.Process_Time > 5)]

#[['FileName'],['Process'],['Workbar'], ['TimeIn'], ['TimeOut'],['Process_Time']]

#drop bad values

#ProdData3 = ProdData2.drop(ProdData2['Process Time' < 0].index)

ProdData2.to_csv('cleanedData.csv')
ProdDataSelection.to_csv('cleanedData2.csv')
ProdDataFaults.to_csv('Issues.csv')