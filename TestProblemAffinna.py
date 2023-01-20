import pandas as pd
def clean_data():
    df = pd.read_csv("https://raw.githubusercontent.com/DanRossLi/TestProblem/main/TestData.csv")
    df_drop = ['Qty', 'Price Level', 'Seatblock1', 'Price Type', 'Resale Difference', 'Resale Date',
               'Resale Per Ticket']
    df.drop(df_drop, inplace=True, axis=1)
    df_double = df['Resale Value'].str.replace('$', '', regex=True).replace(',', '', regex=True).astype('double')
    total = df_double.sum()
    print(df)
    print("Total resale value is:", total)
if __name__ == '__main__':
    clean_data()