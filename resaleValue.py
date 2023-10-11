import pandas as pd
import os

def clean_and_summarize_csv(input_file):
    df = pd.read_csv(input_file)
    df.dropna(inplace=True)
    total_resale_value = df["Resale Value"].sum()
    resale_value_by_item = df.groupby("Item")["Resale Value"].sum()
    return total_resale_value, resale_value_by_item

def write_result_to_file(result, output_file):
    with open(output_file, "w") as file:
        file.write(result)

def main():
    input_file = "TestData.csv"
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)
    total_resale_value, resale_value_by_item = clean_and_summarize_csv(input_file)
    write_result_to_file(f"Total Resale Value: {total_resale_value}", os.path.join(output_directory, "total_resale_value.txt"))
    write_result_to_file("Resale Value by Item:\n" + resale_value_by_item.to_string(), os.path.join(output_directory, "resale_value_by_item.txt"))

if __name__ == "__main__":
    main()
