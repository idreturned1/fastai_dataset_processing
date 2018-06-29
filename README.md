# fastai_dataset_processing

1. Reaname<br>
	a. Description<br>
		Renames the data files for all classes in the format - "class-name.image-number.jpg" (fast.ai format)

	b. Instructions<br>
		1. Open rename.py in any editor.<br>
		2. Add the path to the directory containing the class folders to the PATH variable.<br>
		3. Run the file. The script works for multiple classes as well.


2. Dataset Split<br>
	a. Descriptiton<br>
		Split the data randomly into train, test and valid folders. Can be used when we have directories of classes containing images but they are not seperated into test, train and valid drectories. The script automatically creates the test, valid and train  folders, each containing the class folders with appropriate randomly selected data.

	b. Instructions<br>
		1. Open dataset-split.py in any editor.<br> 
		2. Add the path to the directory containing the class folders as the PATH variable.<br>
		3. Add the path to the directory where you want to store the dataset as DATASETPATH variable.<br>
		4. Set the percentage of test set in ratio as testRatio variable.<br>
		5. Set the percentage of valid set in ratio as validRatio variable.<br>
		6. Run the file. The script works for multiple classes as well.
  
	NOTE - For spliting to work, the images must be in the format specified by the rename.py format. It is recomended to run the rename.py script before using this script. 

  
