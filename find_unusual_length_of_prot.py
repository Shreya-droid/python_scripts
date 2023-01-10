import os
import pandas as pd

df=pd.DataFrame()

file=pd.read_csv("reordered_core_genome.csv")
huge_prot=open("huge_prot_wrt_org.txt",'w+')

col_names=list(file[:0])[1:-1]
print(len(col_names))
     
for org in col_names:
    col=file[org]
    starts=[]
    ends=[]
    length=[]
    
    for row in col:
        val_li=list(row.split("--"))
        start=val_li[1]
        end=val_li[2]
        length_prot=float(end)-float(start)
        starts.append(float(start))
        ends.append(float(end))
        length.append(length_prot)
                    
        zip_all=list(zip(starts,ends,length))
        
        if(length_prot >= float(5000)):
            print(val_li[0] + " has a huge length in " + org + ".This seems fishy" + ":" + str(length_prot) + ".\n")
            huge_prot.write(val_li[0] + " has a huge length in " + org + ".This seems fishy" + ":" + str(length_prot) + ".\n")
        else:
            continue
    
    df[org]=zip_all    

df.to_csv("check_weirdo.csv",index=True)
huge_prot.close()

