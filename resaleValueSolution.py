import pandas as pd
import locale

# Set the locale for US currency formatting
try:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")  # UNIX-based systems
except locale.Error:
    locale.setlocale(locale.LC_ALL, "en_US")  # Windows systems


def read_and_clean_csv(file_path):
    # Read CSV file
    df = pd.read_csv(file_path)

    # Data Cleaning Steps
    df["Resale Value"] = (
        df["Resale Value"].replace(r"[\$,]", "", regex=True).astype(float)
    )

    return df


def calculate_total_resale_value(df):
    total_resale_value = df["Resale Value"].sum()
    return total_resale_value


def calculate_resale_value_by_item(df):
    resale_value_by_item = df.groupby("Item")["Resale Value"].sum()
    return resale_value_by_item


def main():
    file_path = "TestData.csv"

    df = read_and_clean_csv(file_path)
    total_resale_value = calculate_total_resale_value(df)
    resale_value_by_item = calculate_resale_value_by_item(df)

    # Formatting and printing the total resale value
    formatted_total_resale_value = locale.currency(total_resale_value, grouping=True)
    print("\nTotal Resale Value:", formatted_total_resale_value)

    # Formatting and printing the resale value by item
    print("\nResale Value by Item:")
    for item, value in resale_value_by_item.items():
        formatted_value = locale.currency(value, grouping=True)
        print(f"{item}: {formatted_value}")

    print()


if __name__ == "__main__":
    main()
