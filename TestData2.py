import csv

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def clean_data(data):

    cleaned_data = [row for row in data if all(row.values())]
    return cleaned_data

def summarize_data(data, column_name, group_by_column):
    total_sum = 0
    resale_value_by_item = {}
    
    for row in data:
        if column_name in row:
            value = row[column_name].replace('$', '') #Removing the $ so I can print the values accurately.
            try:
                total_sum += float(value)
                

                item = row[group_by_column]
                resale_value = float(value)
                resale_value_by_item[item] = resale_value_by_item.get(item, 0) + resale_value
                
            except ValueError:
                pass  
    
    return total_sum, resale_value_by_item


csv_file_path = "TestData.csv"
selected_column = "Resale Value"  
group_by_column = "Item"

#specifying file path for the .csv file and column's I require


data = read_csv(csv_file_path)

if data:

    cleaned_data = clean_data(data)

    
    total_sum, resale_value_by_item = summarize_data(cleaned_data, selected_column, group_by_column)

   
    print(f"Total sum of '{selected_column}': ${total_sum:.2f}")
    

    print("Resale value by item:")
    for item, resale_value in resale_value_by_item.items():
        print(f"{item}: ${resale_value:.2f}")
else:
    print("Error reading the CSV file.")
