import os, pandas as pd

Data=pd.read_csv("finalblast_protein_coregenome.csv")

file_to_save=open("coregenome_stat.txt",'w+')

orgi=[]
sum_nucl=0
len_list=len(list(Data[:0])[1:-1])
print("total number of organisms in coregenome: ",len_list)

for org in list(Data[:0])[1:-1]:

    org_col=Data[org]
    zeros=0
    ones=0
    sum_len=0
    for row in org_col:
        li = list(row.split("--"))
        nucl_len = abs((float(li[2]) - float(li[1])))
        sum_len = sum_len + nucl_len
        if li[3]=='0':
            zeros+=1
        else:
            ones+=1
            
    print("Zerors for "+ org + ":",zeros)
    print("Ones for "+ org + ":",ones)
    print("total nucleotide for " + org + ":",sum_len)
    sum_nucl=sum_nucl+sum_len
    orgi.append(sum_len)
    
orgi.sort()
mid=len(orgi) // 2
median=(orgi[mid]+orgi[~mid]) / 2   
    
print("total number of nucleoitides in coregenome: ",sum_nucl)
print("mean nucleotide: ",sum_nucl/len_list)
print(orgi)
print("median nucleotide in coregenome", str(median))

file_to_save.write("total number of organisms in coregenome: " + str(len_list) + "\n Zerors for "+ org + ":" + str(zeros) + "\n Ones for "+ org + ":" + str(ones) + "\n total nucleotide for " + org + ":" + str(sum_len) + "\n total number of nucleoitides in coregenome: " + str(sum_nucl) + "\n mean nucleotide: " + str(sum_nucl/len_list) + "\n median nucleotide in coregenome: " + str(median) + "\n")
file_to_save.close()

