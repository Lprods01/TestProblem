## This problem can be solved via "CS" or "DS"
# In general, pick one path and proceed
# Solved this with DS operations

import pandas as pd 
import numpy as np
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="specify input file name")

def main():
    args = parser.parse_args()
    df=pd.read_csv(args.file)

    df_melt=df.melt(id_vars=['transId'])
    df_melt=df_melt[['transId', 'value']].dropna()

    df_melt[['description','section', 'row', 'seat']] = df_melt['value'].str.split(':',expand=True)
    df_melt[['seat1', 'seat2']] = df_melt['seat'].str.split(',',expand=True)
    df_melt['seat1'] = df_melt['seat1'].astype('int')
    df_melt['seat2'] = df_melt['seat2'].astype('int')

    df_melt['seatmin'] = np.minimum(df_melt['seat1'], df_melt['seat2'])
    df_melt['seatmax'] = np.maximum(df_melt['seat1'], df_melt['seat2'])

    df_melt['seatlist'] = df_melt.apply(lambda row: list(range(row['seatmin'], row['seatmax']+1)), axis = 1)

    df_melt = df_melt.drop(['seat1', 'seat2', 'seatmin', 'seatmax'], axis = 1)
    df_final = df_melt.explode('seatlist')

    df_final.to_csv("seat_transactions_sh.csv", index=False)

if __name__ == "__main__":
    main()