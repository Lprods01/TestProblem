import pandas as pd


def cleanData():
    # Reads in a CSV file from the URL provided
    df = pd.read_csv(
        "https://raw.githubusercontent.com/Lprods01/TestProblem/main/TestData.csv")

    # Drops the columns that we do not need in order to clean up the code
    df = df.drop(columns=['Qty', 'Item', 'Price Level', 'Price Type',
                 'Resale Per Ticket', 'Resale Difference', 'Resale Date'])

    # Drops the dollar sign and commas from the Resale Value column then converts the numbers to a float type
    df['Resale Value'] = df['Resale Value'].str.replace(
        '$', '', regex=False).str.replace(',', '', regex=False).astype('float')

    # Adding up the resale values and prints the total resale value
    totalValue = df['Resale Value'].sum()
    print("Total Resale Value:", totalValue)


def itemTotal():
    # Reads in a CSV file from the URL provided
    df = pd.read_csv(
        "https://raw.githubusercontent.com/Lprods01/TestProblem/main/TestData.csv")

    # Drops the dollar sign and commas from the Resale Value column then converts the numbers to a float type
    df['Resale Value'] = df['Resale Value'].str.replace(
        '$', '', regex=False).str.replace(',', '', regex=False).astype('float')

    # Sorts the data by their item then sums the resale value for each group, then prints out the result for each item
    item_totals = df.groupby('Item')['Resale Value'].sum().reset_index()
    print(item_totals)


if __name__ == '__main__':
    # Runs cleanData and itemTotal
    cleanData()
    itemTotal()
