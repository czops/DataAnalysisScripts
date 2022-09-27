import math
import collections

import glob
from csv import reader
from pathlib import Path
#from Reports import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

import csv


df = ['Workbar', 'Process','FileName','Part Number 1', 'Qty 1', 'Part Number 2', 'Qty 2','Part Number 3', 'Qty 3', 'Part Number 4', 'Qty 4', 'Part Number 5', 'Qty 5']

csv_files = glob.glob("*.csv")
print(csv_files)

csv_data = []

def sort_data(list_of_csv):
    
    
    for file in list_of_csv:
        #function here to got through and sort data into single file
        with open(file) as file_obj:
            reader = csv.reader(file_obj)
            for row in reader:
                csv_data.append(row)

#    return(csv_data)

sort_data(csv_files)

def add_to_workbook(data):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save('Consolidated.xlsx')

add_to_workbook(csv_data)

