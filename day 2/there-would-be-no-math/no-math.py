import csv
import numpy

totalNeeded = 0
totalRows = 0

with open('input.csv', 'rb') as csvread:
	sheetreader = csv.reader(csvread, delimiter = ',', quotechar = '\"')
	
	for row in sheetreader:
		dimensions = row[0].split('x')
		dimensions[0] = int(dimensions[0])
		dimensions[1] = int(dimensions[1])
		dimensions[2] = int(dimensions[2])

		lengthwidth = dimensions[0] * dimensions[1]
		widthheight = dimensions[1] * dimensions[2]
		heightlength = dimensions[2] * dimensions[0]

		smallestside = min([lengthwidth, widthheight, heightlength])

		totalNeeded += (2 * lengthwidth) + (2 * widthheight) + (2 * heightlength)
		totalNeeded += smallestside
		totalRows += 1

print totalNeeded
print totalRows
