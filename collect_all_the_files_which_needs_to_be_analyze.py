import os
import pandas as pd
list_of_files = []
rootdir = input("enter the rootdir : ")
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('_to_be_analyze.csv'):
            list_of_files.append(file)

dataframes = []
for file in list_of_files:
    file_subdr = file.split('_')[0]
    root = os.path.abspath(file_subdr)
    os.chdir(root)
    read_file = pd.read_csv(file)
    dataframes.append(read_file)
    curr_dir = input("enter the root where folder bacterial_subgroups present: ")
    os.chdir(curr_dir)
df = pd.concat(dataframes)
df.head()
df.to_csv('find_in_Doric.csv')
