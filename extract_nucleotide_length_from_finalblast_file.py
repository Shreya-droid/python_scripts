import os, pandas as pd

Data=pd.read_csv("finalblast_protein_coregenome.csv")

for org in list(Data[:0])[1:-1]:
    org_col=Data[org]
    zeros=0
    ones=0
    sum_len=0
    for row in org_col:
        li = list(row.split("--"))
        nucl_len = float(li[2]) - float(li[1])
        sum_len = sum_len + nucl_len
        if li[3]=='0':
            zeros+=1
        else:
            ones+=1
    print("Zerors for "+ org + ":",zeros)
    print("Ones for "+ org + ":",ones)
    print("total nucleotide for " + org + ":",sum_len)