import pandas as pd
import os

def clean_and_summarize_csv(input_file):
    df = pd.read_csv(input_file)
    df.dropna(subset=["Resale Value"], inplace=True)
    df["Resale Value"] = df["Resale Value"].str.replace('[$,]', '', regex=True).astype(float)
    total_resale_value = df["Resale Value"].sum()
    resale_value_by_item = df.groupby("Item")["Resale Value"].sum().reset_index()
    return total_resale_value, resale_value_by_item

def write_result_to_file(result, output_file):
    with open(output_file, "w") as file:
        file.write(result)

def main():
    input_file = "TestData.csv"
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)

    total_resale_value, resale_value_by_item = clean_and_summarize_csv(input_file)

    total_resale_value_output_file = os.path.join(output_directory, "ResaleValueTotal.csv")
    resale_value_by_item_output_file = os.path.join(output_directory, "ResaleValueByItem.csv")

    total_resale_value_df = pd.DataFrame({"Resale Value Total": [total_resale_value]})
    total_resale_value_df.to_csv(total_resale_value_output_file, index=False)

    resale_value_by_item.to_csv(resale_value_by_item_output_file, index=False)

if __name__ == "__main__":
    main()
