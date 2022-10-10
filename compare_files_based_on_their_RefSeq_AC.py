import os
import glob
import pandas as pd
import numpy as np
database= pd.read_excel('Gene_Strand_Bias_Database.xlsx')
list_dbase = []
for line in database['RefSeq_AC']:
    line = str(line)
    search = 'NC_'
    if search in line:
       start = line.find('NC_')
    else:
       start = line.find('NZ_')
    end = line.find('.')
    Acc_no = line[start:end]
    list_dbase.append(Acc_no)
for file in glob.glob('*.csv'):
    file_open = pd.read_csv(file)
    list_file = []
    for line in file_open['Replicons']:
        line = str(line)
        search = 'NC_'
        if search in line:
            start = line.find('NC_')
        else:
            start = line.find('NZ_')
        end = line.find('.')
        Acc_no = line[start:end]
        list_file.append(Acc_no)
file_open['RefSeq_AC'] = list_file
count_common = list(set(list_file)&set(list_dbase))
file_found = file_open[file_open.RefSeq_AC.isin(count_common)]
file_found.to_csv(file.split('.csv')[0]+ '_found_by_AC_no_inDB.csv')
unique =(np.setdiff1d(file_open['RefSeq_AC'], file_found['RefSeq_AC']))
file_nr = file_open.drop_duplicates('RefSeq_AC')
file_nr.to_csv('non_redundant_' + file)
file_Analyze = file_nr[file_nr.RefSeq_AC.isin(unique)]
file_Analyze.to_csv(file.split('.csv')[0] + '_to_be_analyze.csv')
