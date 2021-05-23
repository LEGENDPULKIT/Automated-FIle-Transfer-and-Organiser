import os
import shutil

#get the source and the detination
source=input("Enter Source folder path: ")
path=input("enter the destination path : ")


source=source+'/'
path=path+'/'

#get the list of all files inside source folder
list_of_files=os.listdir(source)

for file in list_of_files:
    shutil.move((source+file),path)

list_of_files=os.listdir(path)

#go through each and every file 
for file in list_of_files:
    name,ext=os.path.splitext(file)

    #store the ext
    ext=ext[1:]

    if ext=='':
        continue

    #move the file 
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)