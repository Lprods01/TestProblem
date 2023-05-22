import csv
import pandas as pd
import numpy as np

def cleanData():
    df = pd.read_csv('TestData.csv')

    to_drop = ['Price Level', 'Price Type', 'Resale Per Ticket', 'Resale Difference', 'Resale Date', 'Seatblock1']

    df.drop(columns = to_drop, inplace = True)

    print(df)
    
def totalResale():
    df = pd.read_csv('TestData.csv')#placing csv data into pandas

    currency = df['Resale Value'].replace('[,\$]', '', regex = True).astype(float)#replacing all "$" and "," with a space to calculate the sum on numeric values
    rv = currency.sum()#calculating sum of "Resale Value" column

    #dataframe for total resale value
    resale = {'Total Resale Value': [rv]}
    dataFrame = pd.DataFrame(resale)
    print(dataFrame)


def resaleByitem():
    df = pd.read_csv('TestData.csv')#placing csv data into pandas

    currency = df['Resale Value'].replace('[,\$]', '', regex = True).astype(float)#replacing all "$" and "," with a space to calculate the sum on numeric values

    #summing each item's resale value 
    sum_F01 = currency.loc[df['Item'] == 'F01'].sum()
    sum_F02 = currency.loc[df['Item'] == 'F02'].sum()
    sum_F03 = currency.loc[df['Item'] == 'F03'].sum()
    sum_F04 = currency.loc[df['Item'] == 'F04'].sum()
    sum_F05 = currency.loc[df['Item'] == 'F05'].sum()
    sum_F06 = currency.loc[df['Item'] == 'F06'].sum()
    sum_F07 = currency.loc[df['Item'] == 'F07'].sum()

    #dataFrame for all resale items
    print("Resale By Item")
    rbi = {'Item':['F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07'], 'Resale($)':[sum_F01, sum_F02, sum_F03, sum_F04, sum_F05, sum_F06, sum_F07]}
    dataFrame = pd.DataFrame(rbi)
    print(dataFrame)


cleanData()
totalResale()
resaleByitem()

            