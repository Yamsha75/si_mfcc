import os
import numpy as np
import pandas as pd

FOLDER_MFCC = 'MFCC\\'
FOLDER_DATASET = 'DATASET\\'

print('mfcc numpy array files to one numpy array file')
print('labels to csv')

if os.path.isdir(FOLDER_MFCC):
    files = os.listdir(FOLDER_MFCC)
    n_files = len(files)
    print('found ' + str(n_files) + ' files')
    if n_files > 0:
        if not os.path.isdir(FOLDER_DATASET):
            os.mkdir(FOLDER_DATASET)
        labels = []
        dataset = []
        for filename in files:
            # labels
            if int(filename[-10:-9]) % 2 == 0:
                sex = 'f'
            else:
                sex = 'm'
            emotion = int(filename[-23:-21]) - 1
            labels.append((sex, emotion))

            # data files to single file
            filepath = (FOLDER_MFCC + filename)
            data = np.load(filepath)
            dataset.append(data)
        
        # save to files
        labels_df = pd.DataFrame(labels, columns=('sex', 'emotion'))
        labels_df.to_csv(FOLDER_DATASET + 'labels.csv')
        dataset_arr = np.array(dataset)
        np.save(FOLDER_DATASET + 'dataset.npy', dataset)
        print('done')
    else:
        print('dir is empty!')
else:
    print('dir with mfcc.npy files not found!')