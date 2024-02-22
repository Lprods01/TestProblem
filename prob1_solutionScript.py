import pandas as pd
import os

def process_file(file_path):
    # Loading the dataset
    data = pd.read_csv(file_path)
    
    # Convert 'Resale Value' from string to numeric
    data['Resale Value Numeric'] = data['Resale Value'].replace('[\$,]', '', regex=True).astype(float)
    
    # Calculate the total resale value
    total_resale_value = data['Resale Value Numeric'].sum()
    formatted_total_resale_value = "${:,.2f}".format(total_resale_value)
    
    # Calculate the total resale value by item
    total_resale_value_by_item = data.groupby('Item')['Resale Value Numeric'].sum()
    formatted_resale_values_by_item = total_resale_value_by_item.apply(lambda x: "${:,.2f}".format(x)).to_dict()
    
    # Prepare output file paths
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_total_path = f"{base_name}_total_resale_value.txt"
    output_by_item_path = f"{base_name}_resale_value_by_item.txt"
    
    # Output total resale value to file
    with open(output_total_path, 'w') as f:
        f.write(f"Total Resale Value: {formatted_total_resale_value}\n")
    
    # Output resale value by item to file
    with open(output_by_item_path, 'w') as f:
        for item, value in formatted_resale_values_by_item.items():
            f.write(f"{item}: {value}\n")

# Specify the directory containing the files to process
input_directory = 'C:/Users/ambat/TestProblem'

# Process each file in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_directory, filename)
        process_file(file_path)
        print(f"Processed {filename}")