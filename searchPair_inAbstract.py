"""This small chunk of code search for specific pair of term in pubmed downloaded abstract(pubmed format)
   code written on : 14-01-2023
   credits to Shreya Sharma """


term1=input("enter your first term to be searched: ")
term2=input("enter your second term to be searched: ")
exclude=[];
for substring in df['Abstract']:
    if term1.lower() in substring.lower() and term2.lower() in substring.lower():
        exclude.append(df[df['Abstract']==substring].index.values[0])
#print(exclude)
print(len(exclude))
combined  = pd.DataFrame()##create an empty dataframe
for ind in exclude:
    combined = pd.concat([combined, df[df['Abstract']==df['Abstract'].iloc[ind]]], ignore_index=True)
combined.to_csv('xyz.csv') 

