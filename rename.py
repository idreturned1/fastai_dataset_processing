import os

def increment_file_numbers(directoryPath, className):
    print (directoryPath)
    fileCount = 0
    
    for fileName in os.listdir(directoryPath):
        fileCountString = str(fileCount)
        newName = directoryPath+"/"+className+"."+fileCountString+".jpg"
            
        print("Old name: ",fileName)
        print("New name: ",className+"."+fileCountString+".jpg")
        
        os.rename(directoryPath+"\\"+fileName,newName )
        fileCount += 1

PATH = "" #Path of the directory containing class folders
		  #Eg: C:/Users/Administrator/Desktop/dogscats
dirPath = os.path.abspath(PATH) 
for className in os.listdir(dirPATH):
    increment_file_numbers(dirPATH+"\\"+className, className)


