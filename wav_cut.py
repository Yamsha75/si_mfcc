import os
import wave
import shutil

FOLDER_RAW = 'DATASET_RAW\\'
FOLDER_CUT = 'DATASET_CUT\\'

cut_len = 2.910 # dlugosc do ktorej zostanie przyciety plik [s]

print('cutting raw audio files to ' + str(cut_len) + 's')
if os.path.isdir(FOLDER_RAW):
	files = os.listdir(FOLDER_RAW)
	n_files = len(files)
	print('found ' + str(n_files) + ' files')
	if n_files > 0:
		if not os.path.isdir(FOLDER_CUT):
			os.mkdir(FOLDER_CUT)
		n_cut = 0
		for file in files:
			if os.path.isfile(FOLDER_RAW + file):
				audio_raw = wave.open(FOLDER_RAW + file, 'rb')
				
				n_channels = audio_raw.getnchannels()
				samp_width = audio_raw.getsampwidth()
				framerate  = audio_raw.getframerate()
					
				n_frames = int(cut_len * framerate)
				frames = audio_raw.readframes(n_frames)
				
				audio_raw.close()
				
				audio_cut = wave.open(FOLDER_CUT + file, 'wb')
				
				audio_cut.setnchannels(n_channels)
				audio_cut.setsampwidth(samp_width)
				audio_cut.setframerate(framerate)
				audio_cut.setnframes(n_frames)
				
				audio_cut.writeframesraw(frames)
				
				audio_cut.close()
				n_cut = n_cut + 1
				print('cut ' + str(n_cut) + '/' + str(n_files) + ' files', end='\r')
		print('\ndone')
	else:
		print('dir is empty!')
else:
	print('dir with raw audio files not found!')

