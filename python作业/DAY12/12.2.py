import argparse
import pandas
argparse = argparse.ArgumentParser()
argparse.add_argument('--Path',type=str,help='csv路径(str)')
argparse.add_argument('--number',type=str,help='删除列名(str)')
args = argparse.parse_args()
df = pandas.read_csv(args.Path)
df = df.drop(columns = args.number)
print(df)