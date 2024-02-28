#!/usr/bin/python3
'''
This program will read all csv files in the directory and subdirectories in which it is run to find the total
of all of the resale values of all items, and the total resale value of all item types. 

Once found, it writes these values in csv format to text files, one for each answer.

I'm not certain if the problem statement is asking for each itemized resale value total to be written to a new file, 
or for both of the two answers to be written to separate files. I will write code solutions for both scenarios but 
comment out the code solution for the prior case (printing each itemized value total to a text file).
'''
import csv
import os

total_resale_values = 0
itemized_total_resale_values = {}
errors = []
banner = "\n"+"*"*40+"\n"

def cash_value_to_float(cash_value_str):
    try:
        # remove currency symbols and separators
        cleaned_value_str = cash_value_str.replace('$', '').replace(',', '')
        # make float
        cash_value_float = float(cleaned_value_str)
        cash_value = round(cash_value_float, 2)
    except Exception as e:
        errors.append(f"{banner}ERROR \nCould not handle {e}{banner}\n")
    return cash_value


if __name__ == "__main__":
    for root, dirs, files in os.walk('.'):
        for file in files:
            if os.path.splitext(file)[1] == '.csv' and 'total_resale' not in file:

                full_path = os.path.join(root,file)
                try:
                    with open(full_path, newline='') as csv_file:
                        reader = csv.DictReader(csv_file)
                        for row in reader:
                            resale_value = cash_value_to_float(row['Resale Value'])
                            if resale_value == None: print("oops!")
                            if str(row['Item']) in itemized_total_resale_values.keys():
                                itemized_total_resale_values[str(row['Item'])] += resale_value
                            else: itemized_total_resale_values[str(row['Item'])] = resale_value
                            total_resale_values += resale_value
                except Exception as e:
                    errors.append(f"{banner}ERROR on file: {file}\nCould not handle {e}{banner}\n")
    
    # round totals to account for floating point errors
    itemized_total_resale_values = {key: round(value, 2) for key, value in itemized_total_resale_values.items()}
    total_resale_values = round(total_resale_values, 2)
    
    # write info to csv files
    with open("itemized_total_resale.csv", 'w', newline = '') as csv_file:
        fieldnames = ['Item', 'Total Resale Value']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in itemized_total_resale_values:
            writer.writerow({'Item': str(item), 'Total Resale Value': itemized_total_resale_values[item]})
    
    # # I really can't imagine you would want to do it this way but the wording of the problem statement COULD be interpreted
    # # as instructing me to write a file for each resale value... So I wrote a variation that would do that.
    # for item in itemized_total_resale_values:
    #     with open(f"{item}_total_resale.csv", 'w', newline = '') as csv_file:
    #         fieldnames = ['Item', 'Total Resale Value']
    #         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #         writer.writeheader()
    #         writer.writerow({'Item': str(item), 'Total Resale Value': itemized_total_resale_values[item]})

    with open("total_total_resale.csv", 'w', newline = '') as csv_file:
        fieldnames = ['Item', 'Total Resale Value']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Item': '*', 'Total Resale Value': total_resale_values})
    
    # write error log
    with open("ErrLogs.txt", 'w') as f:
        for error in errors:
            f.write(error)


    # printed output to console
    print(f"\033[4mItem\t|\tTotal Resale Value\033[0m")
    for item in itemized_total_resale_values:
        print(f"{item}\t|\t{itemized_total_resale_values[item]}")
    print(f"{banner}Total of all Resale Values: {total_resale_values}{banner}")
    for error in errors:
        print(error)