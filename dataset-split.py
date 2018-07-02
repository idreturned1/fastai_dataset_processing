import os
import random
  
#PATH is the location of directory containing images in seperate class directories
#Eg: C:/Users/Administrator/Desktop/dogscats
#DATASETPATH is the directory location where you want the data-set to be created  
#Eg: C:/Users/Administrator/Desktop/dogscats-dataser

PATH = os.path.abspath('.')
DATASETPATH = os.path.abspath('.')
testRatio = 0.2 #define the ratio of test cases
validRatio = 0.2 #define the number of valid cases

if not os.path.exists(DATASETPATH+'/'+'test'):
        os.makedirs(DATASETPATH+'/'+'test')
		
directories = ['train','valid']
for dir in directories:
    if not os.path.exists(DATASETPATH+'/'+dir):
        os.makedirs(DATASETPATH+'/'+dir)
        for name in os.listdir(PATH):
            os.makedirs(DATASETPATH+'/'+dir+'/'+name)
    
for className in os.listdir(PATH):
    itemNumber = len(os.listdir(PATH+"/"+className))
    testCount = int(testRatio*itemNumber)
    validCount = int(validRatio*itemNumber)
    testIndex = []
    validIndex = []
    
    for i in range(0,testCount):
        testIndex.append(random.randint(0,itemNumber))
    
    while(len(validIndex) != validCount):
        num = random.randint(0,itemNumber)
        if num not in testIndex:
            validIndex.append(num)       
    
        
    for itemName in os.listdir(PATH+"/"+className):
        temp = itemName.split(".")
        
        if int(temp[1]) in testIndex:
            os.rename(PATH+"/"+className+"/"+itemName, DATASETPATH+"/"+"test"+"/"+itemName)
        elif int(temp[1]) in validIndex:
            os.rename(PATH+"/"+className+"/"+itemName, DATASETPATH+"/"+"valid"+"/"+className+"/"+itemName)
        else:
            os.rename(PATH+"/"+className+"/"+itemName, DATASETPATH+"/"+"train"+"/"+className+"/"+itemName)
    

    
