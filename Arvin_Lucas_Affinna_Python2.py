import pandas as pd

#To load in csv, use pd.read_csv(r"[file path]")

if __name__ == "__main__":

    df = pd.read_csv(r"C:\Users\the8t\Desktop\memes\sampledata\AffinnaTestData.csv")
    #This solution is for a single .csv file
    #My core process would work for any number of .csv files, but in order to write a complete solution,
    #I'd need to know exactly how the file paths are being provided.
    #Is the user entering them?
    #Is there a file containing file paths to the .csvs in need of processing?
    #Additionally, I would need to know every possible Item type BEFORE writing a solution.

    #This solution is the best I could produce with the information provided by the README.

    #The following process will retrieve the set of items in the CSV.
    #I need this because I am not aware of all the possible types of items and am not counting them manually.
    #In the future, something like this would not be necessary. I would be informed of all possible items.
    #It is ultimately commented out b/c I only need its results to write the solution, not to run it.

    """
    unique_items = set()

    for x in range(len(df.index)):
        unique_items.add(df.iat[x, 1])

    print(unique_items)
    """

    #Item types present in this csv are: FO6, F03, F05, F01, F02, F04 and F07

    #print()
    #print(type(df.iat[1, 1]))
    #item type is stored as a string in the DataFrame

    # Create 8 variables to store the requested data
    resale_total = 0.0
    resale_f01 = 0.0
    resale_f02 = 0.0
    resale_f03 = 0.0
    resale_f04 = 0.0
    resale_f05 = 0.0
    resale_f06 = 0.0
    resale_f07 = 0.0

    #print(df.iat[2151, 4])
    #print(type(df.iat[2151, 4]))
    #Some values appear as "#######" in the .csv I downloaded for use but are valid numbers stored as strings


    """Below is my core process. This will work for any .csv of any size, provided there are
    not additional items (Ex: F08) that were not in the example data"""
    for x in range(len(df.index)):
        resale_total += (int(''.join(c for c in df.iat[x, 4] if c.isdigit())))
        #All the junk above is what I have to go through to retrieve usable data from the .csv
        #This wouldn't be precise in all concievable situations where you must parse digits from a string.
        #It will work for the particular format of the data of the Resale Value column.
        if(df.iat[x, 1] == "F01"):
            resale_f01 += (int(''.join(c for c in df.iat[x, 4] if c.isdigit())))
        elif(df.iat[x, 1] == "F02"):
            resale_f02 += (int(''.join(c for c in df.iat[x, 4] if c.isdigit())))
        elif(df.iat[x, 1] == "F03"):
            resale_f03 += (int(''.join(c for c in df.iat[x, 4] if c.isdigit())))
        elif(df.iat[x, 1] == "F04"):
            resale_f04 += (int(''.join(c for c in df.iat[x, 4] if c.isdigit())))
        elif(df.iat[x, 1] == "F05"):
            resale_f05 += (int(''.join(c for c in df.iat[x, 4] if c.isdigit())))
        elif(df.iat[x, 1] == "F06"):
            resale_f06 += (int(''.join(c for c in df.iat[x, 4] if c.isdigit())))
        elif(df.iat[x, 1] == "F07"):
            resale_f07 += (int(''.join(c for c in df.iat[x, 4] if c.isdigit())))
        else:
            print("You should never see this.")

    #All the resale value variables initially store the values in pennies
    #This is a common convention, to store currency as a whole number of its smallest whole unit

    #I slap the dollar sign in front and divide by 100 to format the final output

    print()
    print("Total resale value: $" +  str(resale_total/100))
    print("Resale value for item F01: $" + str(resale_f01/100))
    print("Resale value for item F02: $" + str(resale_f02/100))
    print("Resale value for item F03: $" + str(resale_f03/100))
    print("Resale value for item F04: $" + str(resale_f04/100))
    print("Resale value for item F05: $" + str(resale_f05/100))
    print("Resale value for item F06: $" + str(resale_f06/100))
    print("Resale value for item F07: $" + str(resale_f07/100))

    total_test = resale_f01 + resale_f02 + resale_f03 + resale_f04 + resale_f05 + resale_f06 + resale_f07
    #Final test to confirm accuracy of the solution.
    #Sum of resale value of individual items should match total resale value
    if(resale_total == total_test):
        print()
        print("Looks like everything adds up right.")

    #At the end of the process, the resale_xx variables store accurate values.
    #They are ready to be reused/saved/exported as needed.
    #Reformatting them to any other necessary format is trivial.

    #example
    resale_f01_save = "$" + str(resale_f01/100)

    #resale_f01_save is now formatted identically to the data in the Resale Value column of TestData.csv
    
