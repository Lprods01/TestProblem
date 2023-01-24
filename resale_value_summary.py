import argparse
import pandas as pd
import os;

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("csv_path", help="Specify the path to the .csv file (or the name if it's in the same directory as this script)")

# helper functions
def make_column_numeric(dataframe: pd.DataFrame, column: str) -> pd.DataFrame:
    # regex matches everything that isn't 0-9, point, and negative sign
    strip_non_digits = dataframe[column].str.replace('[^.0-9\-]', '', regex=True)
    to_float = pd.to_numeric(strip_non_digits, errors="raise")

    dataframe[column] = to_float

def float_to_currency(value: float) -> str:
    return '${:,.2f}'.format(value)

def make_column_currency(dataframe: pd.DataFrame, column: str) -> pd.DataFrame:
    dataframe[column] = dataframe[column].apply(float_to_currency)

# main functions
def get_resale_value_total(dataframe: pd.DataFrame) -> float:
    return dataframe["Resale Value"].sum()

def get_resale_value_per_item(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.groupby(["Item"])["Resale Value"].sum().reset_index()


if __name__ == "__main__":       
    args = argument_parser.parse_args()

    dataframe = pd.read_csv(args.csv_path)
    make_column_numeric(dataframe, "Resale Value")

    resale_total = get_resale_value_total(dataframe);
    print('\nTotal Resale Value:\n  ', float_to_currency(resale_total), "\n")
    
    print("Per Item:\n")
    resale_per_item = get_resale_value_per_item(dataframe)
    make_column_currency(resale_per_item, "Resale Value")
    print(resale_per_item, "\n")
