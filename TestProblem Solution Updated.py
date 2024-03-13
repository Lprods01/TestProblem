"""
Dylan Williams
Affinna Technical Part 2
https://github.com/Lprods01/TestProblem
March, 2024
"""


"""
INPUT to this program:
    > a series of .csv files
OUTPUT of this program:
    > a .txt file containing the total Resale Value of every entry
    > a .txt file containing a dict with the total Resale Value of each unique item
    > for each unique item, a .txt file containing that specific item's total Resale Value
"""

import csv
import os

inDir = "INPUT/"
outDir = "OUTPUT/"
if not os.path.exists(inDir):
    os.makedirs(inDir)
if not os.path.exists(outDir):
    os.makedirs(outDir)




for file in os.listdir(inDir):
    
    with open(inDir+file) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)    #Skip header line containing field/column names. 
    
        totalResaleValue = 0
        itemResVals = {}
        for row in reader:
            resVal = row[4]
            resVal = resVal.replace('$', '')
            resVal = resVal.replace(',', '')
            resVal = float(resVal)

            item = row[1]
            if item in itemResVals:
                itemResVals[item] += resVal
            else:
                itemResVals[item] = resVal

            totalResaleValue += float(resVal)




        #Write results to output files.
        #.txt is used, though this portion can be modified to output .csv files.

        #Each csv file in INPUT will have its own folder in OUTPUT.
        outFileDir = outDir + file + "/"
        if not os.path.exists(outFileDir):
            os.makedirs(outFileDir)
            
        with open(outFileDir + "TotalResaleValue.txt", 'w') as outFile:
            outFile.write(str(totalResaleValue))
            
        #The "Recommendations" section doesn't specify whether (1) all items should be in one file or (2) each item should have its own file.
        #Both solutions are provided.        

        #(1) Output all items to one file.
        with open(outFileDir + "TotalResaleValue by Item.txt", 'w') as outFile:
            for item in itemResVals:
                outFile.write(item + ": " + str(itemResVals[item]) + "\n")

        #(2) Give each item its own file.
        for item in itemResVals:
            with open(outFileDir + item + " TotalResaleValue.txt", 'w') as outFile:
                outFile.write(item + ": " + str(itemResVals[item]))

