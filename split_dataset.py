import os
import random


FOLDER_MFCC = 'MFCC\\'


learning_dataset = []
testing_dataset = []

if os.path.isdir(FOLDER_MFCC):
    files = os.listdir(FOLDER_MFCC)
    n_files = len(files)
    print('Found ' + str(n_files) + ' files')
    for file in files:
        learning_dataset.append(file)

	for i in range(0, int(n_files * 0.2), 1):
		ID = random.randrange(0, len(learning_dataset), 1)
		testing_dataset.append(learning_dataset.pop(ID))

	if not os.path.exists('LEARN\\'):
		os.mkdir('LEARN')

	for file in learning_dataset:
		os.rename('MFCC\\' + file, 'LEARN\\' + file)

	if not os.path.exists('TEST\\'):
		os.mkdir('TEST')

	for file in testing_dataset:
		os.rename('MFCC\\' + file, 'TEST\\' + file)
		
	print('Separated dataset to ' + str(len(learning_dataset)) + ' recordings for learning and ' + str(len(testing_dataset)) + ' for testing')