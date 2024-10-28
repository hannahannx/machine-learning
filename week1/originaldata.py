# Loading the data set and displaying the original dataset
import csv

with open('titanic.csv', 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)

#Checking for missing values of Age and Cabin
csvFile['Age'].fillna(csvFile['Age'].median())


#Summary - the missing values were removed