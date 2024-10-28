# Loading the data set
import csv
with open('titanic_samples.csv', 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
# Inspecting the data
# Displaying original dataset
# Check for any missing values in the Age column and Cabin.
#Handle Missing Values
    #Fill the missing values in the Age column with the median age.
#Data Transformation
    #Discuss the Ticket column:
    #Is there any useful information in the Ticket numbers?
    #Should the Ticket column be retained for analysis or not?
#Final Review
    #Print the cleaned dataset after handling missing values.
    #Summarise the changes made during the cleaning process.