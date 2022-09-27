import glob
from csv import reader

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

import openpyxl

import csv
import sys

#'FileName', removed from fields
fields = ['FileName:', 'Process:', 'Workbar:','TimeOut', 'Part Number 1:', 'Qty 1:', 'Part Number 2:', 'Qty 2:','Part Number 3:', 'Qty 3:', 'Part Number 4:', 'Qty 4:', 'Part Number 5:', 'Qty 5:', 'Steps']
headers = ['FileName','Process','Workbar', 'TimeOut', 'Part Number 1', 'Qty 1', 'Part Number 2', 'Qty 2','Part Number 3', 'Qty 3', 'Part Number 4', 'Qty 4', 'Part Number 5', 'Qty 5']

#add 37 ~ steps to the headers
step_numbers = []
for i in range(0,39):
    step_numbers.append(i)

for i in step_numbers:
    headers.append(i)

print(headers)

csv_files = glob.glob("*.csv")
print(csv_files)
print('===========================================================')

#Empty list & dictionary variable
ZDC_Filename_List = []
FileName_dict = {}
dict_ofFileNames = {}

#function for removing the blank rows in each Report file
def no_blank(fd):
    try:
        while True:
            line = next(fd)
            if len(line.strip()) != 0:
                yield line
    except:
        return

###function to remove empty rows from Reports and merge them into a single dictionary- key items are Filenames like '20220613_124 PM'
###steps are grouped together into a single key item 'Steps'
def RemoveEmptyRows(list_of_csv):
    
    for file in list_of_csv:
        with open(file) as file_obj:
            csv_reader = csv.reader(no_blank(file_obj))
            new_csv = []
            
            ###this step is less than ideal... appends a list of strings to the CSV list of rows
            for row in csv_reader:
                new_csv.append(row)
            
            print(new_csv)

            #define the ZDC Filename Dictionary          
            steps_list = new_csv[13:(14+len(new_csv))]

            FileName_dict = {str(new_csv[2][0]): str(new_csv[2][1]), #FileName
                                str(new_csv[1][0]): str(new_csv[1][1]), #Process
                                str(new_csv[0][0]): str(new_csv[0][1]), #Workbar
                                str(new_csv[3][0]): str(new_csv[3][1]), #PartNumber1:
                                str(new_csv[4][0]): str(new_csv[4][1]), #qty1
                                str(new_csv[5][0]): str(new_csv[5][1]), #PartNumber2
                                str(new_csv[6][0]): str(new_csv[6][1]), #qty2
                                str(new_csv[7][0]): str(new_csv[7][1]), #PartNumber3:
                                str(new_csv[8][0]): str(new_csv[8][1]), #qty3
                                str(new_csv[9][0]): str(new_csv[9][1]), #PartNumber4:
                                str(new_csv[10][0]): str(new_csv[10][1]), #qty4
                                str(new_csv[11][0]): str(new_csv[11][1]), #PartNumber5:
                                str(new_csv[12][0]): str(new_csv[12][1]) #qty5
                                #'Steps': steps_list
                            }
            
            print(steps_list)

            #list of steps
            time_out = ''

            for steps in steps_list:
                print(steps)
                #new_list = list(steps.split(","))
                #print(new_list)
                #list of items in each step
                
                FileName_dict[steps[0]] = steps
                
                if steps[1] == 'Station 51 Unload':
                    time_out = steps[3]
                    print(time_out)
            
            FileName_dict['TimeOut'] = time_out

            print(FileName_dict)

            FileName = str(new_csv[2][1])
            dict_ofFileNames = {FileName:FileName_dict}
            ZDC_Filename_List.append(dict_ofFileNames)        
                    
RemoveEmptyRows(csv_files)

def new_wb(my_list):
    with open('mycsvfile2.csv', 'w', newline = '') as f:
        w = csv.writer(f, headers)
        w.writerow(headers)
        for FileNameD in my_list:
            for ThisDate, values in FileNameD.items():
                w = csv.writer(f, fields)
                row = []
                for k, value in values.items():
                    #this is where the dictionary items are placed into a row for CSV writing
                    row.append(str(value))
                row[3] = FileNameD['TimeOut']
                w.writerow(row)

new_wb(ZDC_Filename_List)

