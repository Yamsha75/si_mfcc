# si_mfcc

Preprocessed dataset:
https://drive.google.com/drive/folders/13PfYy6lgAen7t1Q4u9gT7Y0WkNKw1uDi

* dataset.npy contains 1440 numpy arrays with 290x13 MFCC features arrays.
* labels.csv contains 1440 rows of speaker's sex and emotion. Row numbers correspond to dataset.npy

## How to use

1. Download raw audio dataset from https://zenodo.org/record/1188976#.XPufrogzaUk. We used only audio .wav files.
2. ```python wav_cut.py``` to cut audio files to the same length.
3. ```python wav_to_mfcc.py``` to extract MFCC features from audio files.
4. ```python mfcc_to_numpy.py``` to transform MFCC.npy files into a single DATASET.npy file and labels.csv.
5. ```python ffnn.py``` to create the feed forward neural network, fit the model and evaluate.

Steps 1-4 are optional, you can skip to step 5. if you use the prepared dataset from link above.
