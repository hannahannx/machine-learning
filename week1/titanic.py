# MY EXAMPLE

# Loading the data set
import csv
with open('titanic_sample.csv', 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
