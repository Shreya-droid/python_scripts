import os
import pandas as pd

df=pd.DataFrame()

file=pd.read_csv("reordered_core_genome.csv")

col_names=list(file[:0])[1:-1]
print(len(col_names))

for org in col_names:
    col=file[org]
    rows=[]
    for row in col:
        val_li=list(row.split("--"))
        val=val_li[-1]
        rows.append(val)
    df[org]=rows


df["sum_all_rows"]=df.sum(axis=1)

df.to_csv("append_values.csv",index=True)
