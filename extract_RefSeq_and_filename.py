
import os
base_dir=os.getcwd()

folder=input('Enter the Foldername: ')

os.chdir(base_dir+'/replicons/')
print(os.getcwd())
file_to_write = open(folder + '.txt', 'w+')
file_to_write.write("Filename"+","+"RefSeq"+'\n')
        
for file in os.listdir():
    if file.endswith('.fna'):
        readF=open(file,'r')
        RefSeq=readF.readlines()[0].split(' ')[0].split('>')[1]
        filename=file.rstrip('.fna')
        file_to_write.write(filename+','+ RefSeq +'\n')
        
file_to_write.close()  

