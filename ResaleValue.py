import pandas as pd

# Only keeps the item and resale value columns, and converts the resale values into usable floats
def clean(df):
    df = df[["Item", "Resale Value"]]
    df["Resale Value"] = df["Resale Value"].replace('\$','',regex=True).replace('\,','',regex=True).astype(float)
    return df

# Returns the appropriate string corresponding to task 1.
def totResaleValue(df):
    sum = df["Resale Value"].sum()
    return f"The total resale value is ${sum:,.2f}\n\n"

# Returns the appropriate string corresponding to task 2.
def resaleByItem(df):
    res = ""
    items = df.groupby("Item")
    for item_name, item_df in items:
        sum = item_df["Resale Value"].sum()
        res += f"The total resale value of item {item_name} is ${sum:,.2f}\n\n"
    return res



if __name__ == "__main__":
    df = clean(pd.read_csv("https://raw.githubusercontent.com/Lprods01/TestProblem/main/TestData.csv"))
    
    with open("total_rsv.txt", "w") as file:
        file.write(totResaleValue(df))
    
    with open("rsv_by_item.txt", "w") as file:
        file.write(resaleByItem(df))