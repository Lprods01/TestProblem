import pandas as pd


def cleanData(df):
    cleanDf = df.drop(['Qty', 'Price Level', 'Price Type', 'Resale Per Ticket', 'Resale Difference', 'Resale Date', 'Seatblock1'], axis=1)
    cleanDf['Resale Value'] = cleanDf['Resale Value'].str.replace('$', '', regex=True).str.replace(',', '', regex=True).astype(float)
    return cleanDf


def totalResaleValue(df):
    sum = df['Resale Value'].sum(axis=0)
    print("The total resale value is: ", sum)


def resaleByItem(df):
    groupDf = df.groupby(['Item']).sum()
    print(groupDf)


if __name__ == '__main__':

    df = pd.read_csv("https://raw.githubusercontent.com/Lprods01/TestProblem/main/TestData.csv")
    cleanDf = cleanData(df)
    totalResaleValue(cleanDf)
    resaleByItem(cleanDf)
