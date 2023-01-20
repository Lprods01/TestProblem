import pandas as pd
def clean_data():
    df = pd.read_csv("https://raw.githubusercontent.com/DanRossLi/TestProblem/main/TestData.csv")
    df_drop = ['Qty', 'Price Level', 'Seatblock1', 'Price Type', 'Resale Difference', 'Resale Date',
               'Resale Per Ticket']
    df.drop(df_drop, inplace=True, axis=1)
    df_double = df['Resale Value'].str.replace('$', '', regex=True).replace(',', '', regex=True).astype('double')
    total = df_double.sum()

    print("Total resale value is:", total)

def item_total():
    df = pd.read_csv("https://raw.githubusercontent.com/DanRossLi/TestProblem/main/TestData.csv")
    df['Resale Value']= df['Resale Value'].str.replace('$', '', regex=True).replace(',', '', regex=True).astype('float')
    df.sort_values(["Item"],
                        axis=0,
                        ascending=[False],
                        inplace=True)

    print(df.groupby(['Item'])['Resale Value'].sum().reset_index())
if __name__ == '__main__':

    item_total()
    clean_data()