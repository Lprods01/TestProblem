import pandas as pd
import os
import re
import numpy as np

def dynamic_cleaning(df: pd.DataFrame, process_seatblock: bool = True) -> pd.DataFrame:
    """
    Dynamically cleans the DataFrame based on the content of its columns, with an option to specially process 
    columns similar to 'Seatblock' by separating them into more detailed components. This version ensures the process_seatblock process does not have an existent value
    last part is further split by commas and retains specific new column names. Adds error handling for currency to float conversion, checks for NaNs, and handles 'Unknown' values after processing 'Seatblock'-like columns.

    :param df: The input pandas DataFrame.
    :param process_seatblock: Boolean flag to enable/disable special processing of 'Seatblock'-like columns.
    :return: The cleaned pandas DataFrame.
    """
    for column in df.columns:
        if df[column].empty:
            continue  
        first_value = df[column].dropna().iloc[0]

        if isinstance(first_value, str) and ('$' in first_value):
            df[column] = df[column].replace('[\$,]', '', regex=True).astype(float)
            # Check if conversion to float was successful for all non-NaN values
            if not df[column].apply(lambda x: isinstance(x, float) or pd.isna(x)).all():
                raise ValueError(f"Conversion to float failed in column: {column}")
            # Check for NaN values 
            if df[column].isnull().any():
                raise ValueError(f"NaN values found in column after conversion: {column}")
        
        if process_seatblock and re.search(r'seatblock', column, re.IGNORECASE):
            df[column] = df[column].fillna("Unknown")
            
            splits = df[column].str.extractall(r'([^:]+)').unstack().droplevel(0, axis=1)
            last_part = splits.iloc[:, -1].str.extract(r'([^,]+),([^,]+)')
            
            new_df = pd.DataFrame(index=df.index)
            if len(splits.columns) > 1:
                for idx, col_name in enumerate(['Description', 'Section', 'Row'][:len(splits.columns)-1]):
                    new_df[col_name] = splits.iloc[:, idx]
            
            if not last_part.empty:
                new_df['SeatStart'], new_df['SeatEnd'] = last_part[0], last_part[1]
            
            df = pd.concat([df.drop(columns=[column]), new_df], axis=1)
            
            # Check for empty values
            if new_df.isnull().any().any():
                raise ValueError(f"Unknown values found in column after processing: {column}, index: {new_df[new_df.isnull().any(axis=1)].index[0]}\n{new_df[new_df.isnull().any(axis=1)]}")
    return df

def preprocess_output_data(df: pd.DataFrame, name: str, process_seat_block_column_like: bool = True, output_path: str = '.'):
    """
    Processes the given DataFrame, calculates required statistics, and outputs to specified files.

    :param df: DataFrame to be processed.
    :param name: Base name for the output files.
    :param process_seat_block_column_like: Flag to process 'Seatblock'-like columns.
    :param output_path: Folder to save output files. Defaults to the current folder.
    """
    # Ensure output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Clean the data
    cleaned_df = dynamic_cleaning(df, process_seat_block_column_like)

    # Calculate total resale value
    total_resale_value = cleaned_df['Resale Value'].sum()

    # Calculate total resale value by item
    total_resale_value_by_item = cleaned_df.groupby('Item')['Resale Value'].sum().reset_index()

    # Define output file paths
    cleaned_data_file = os.path.join(output_path, f"{name}_cleaned_data.csv")
    total_resale_value_file = os.path.join(output_path, f"{name}_total_resale_value.csv")
    total_resale_value_by_item_file = os.path.join(output_path, f"{name}_total_resale_value_by_item.csv")

    # Write output files
    cleaned_df.to_csv(cleaned_data_file, index=False)
    pd.DataFrame({'Total Resale Value': [total_resale_value]}).to_csv(total_resale_value_file, index=False)
    total_resale_value_by_item.to_csv(total_resale_value_by_item_file, index=False)

    print(f"Cleaned data saved to {cleaned_data_file}")
    print(f"Total resale value saved to {total_resale_value_file}")
    print(f"Total resale value by item saved to {total_resale_value_by_item_file}")
    
if __name__ == "__main__":
    # Sample run
    # I decided to accept a df over a file path to make the function more flexible
    # on how user can pass the data to be processed.
    # For multiple files, the user can loop through the files and pass the df 
    # and fileName to the function.
    file_path = 'TestData.csv'
    file_name = 'TestData'
    outputh_path = '.'
    df = pd.read_csv(file_path)
    # Note: My reasoning to creating a preprocessing for Seatblock column is that
    # storing strings that could potentially have the wrong format might cause issues in the future
    # Set flag to False if this column has already been processed
    preprocess_output_data(df, file_name, process_seat_block_column_like=True, output_path=outputh_path)