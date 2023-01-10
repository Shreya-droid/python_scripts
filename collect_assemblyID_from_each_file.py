import os 
home_dir = os.getcwd()
folder=input('Enter the Foldername: ')
   
os.chdir(home_dir+'/replicons/')  
print(os.getcwd())
       
file_to_write = open(folder + '_assemb' + '.txt', 'w+')
for file in os.listdir():
    if file.endswith('.fna'):
        filename=file.rstrip('_').replace('GCF','GCA')
        file_to_write.write("_".join(filename.split('_')[:2])+'\n')
        print(os.getcwd())
    else:
        continue
    
file_to_write.close()        
