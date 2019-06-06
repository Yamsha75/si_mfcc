import os
import wave

SRC = 'DATASET_RAW\\03-01-02-01-01-02-01.wav'
OUT = 'dupa.wav'

src = wave.open(SRC, 'rb')
out = wave.open(OUT, 'wb')

frames = src.getnframes()

out.setnchannels(1)
out.setsampwidth(src.getsampwidth())
out.setframerate(src.getframerate())
out.setnframes(frames)

for _ in range(int(frames)):
	bin = src.readframes(1)
	out.writeframesraw(bin[0:2])

src.close()
out.close()