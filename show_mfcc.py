import numpy

PATH = 'MFCC\\03-01-01-01-01-01-01.mfcc.npy'

matrix = numpy.load(PATH)

x = len(matrix)
y = len(matrix[0])

print('size = ' + str(x) + ' x ' + str(y))
print('number of neural network inputs: ' + str(x * y))
print(matrix)