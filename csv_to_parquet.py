import pyarrow.csv as pcsv
import pyarrow.parquet as pq
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="specify path to file")

def csv_to_parquet(filepath):
    csv_file = filepath + '.csv'
    parquet_file = filepath + '.parquet'
    csv = pcsv.read_csv(csv_file)
    pq.write_table(csv, where = parquet_file)    

if __name__ == "__main__":       
    args = parser.parse_args()
    csv_to_parquet(args.filepath)
