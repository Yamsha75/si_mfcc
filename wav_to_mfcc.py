import os
import numpy
import scipy.io.wavfile as wav
import python_speech_features as psf

FOLDER_CUT = 'DATASET_CUT\\'
FOLDER_MFCC = 'MFCC\\'
NFFT = 1200

print('cut audio files to mfcc')
if os.path.isdir(FOLDER_CUT):
	files = os.listdir(FOLDER_CUT)
	n_files = len(files)
	print('found ' + str(n_files) + ' files')
	if n_files > 0:
		if not os.path.isdir(FOLDER_MFCC):
			os.mkdir(FOLDER_MFCC)
		n_mfcc = 0
		for file in files:
			if os.path.isfile(FOLDER_CUT + file):
				rate, sig = wav.read(FOLDER_CUT + file)
				mfcc_feat = psf.mfcc(sig, rate, nfft=NFFT)
				numpy.save(FOLDER_MFCC + file[:-4] + '.mfcc', mfcc_feat)
				
				n_mfcc = n_mfcc + 1
				print('saved ' + str(n_mfcc) + '/' + str(n_files) + ' mfcc files', end='\r')
		print('\ndone')
	else:
		print('dir is empty!')
else:
	print('dir with cut audio files not found!')