####Alert: make sure your coregenome and reference gff both are in same directory and that's your working directory.

import os,pandas as pd
filename = input ("Enter the coregenome filename: ")
print(filename)
    
reference_genome = input ("Enter the reference genome gff filename: ")
print(reference_genome)
    
coregenome=pd.read_csv(filename, sep=',')
df_coregenome=pd.DataFrame(coregenome)
    
ref_gff=pd.read_csv(reference_genome,sep=';',names=["col1", "col2", "col3", "col4","col5","col6","col7","col8","col9"])
ref_df=pd.DataFrame(ref_gff)

sum_len=0.0    
for protein in df_coregenome[reference_genome.rstrip(".gff")]:
    protein=protein.split("--")[0]
    
    for Name in ref_df['col4']:
        if (str(Name).startswith("Name")) and (Name.split("=")[1]==protein):
            index_row=ref_df[ref_df['col4']==Name].index[0]
            cds_start_end=list((ref_df['col1'][index_row]).split("\t"))[3:5]
            start=cds_start_end[0]
            end=cds_start_end[1]
            cds_length=float(end)-float(start)
            print(cds_length)

            sum_len = sum_len + cds_length

print('total protein coding gene length: ',sum_len)