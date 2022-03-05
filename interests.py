from person import Person
import csv
file = open('mockdatabase.csv')
csv_reader = csv.reader(file)
header = next(csv_reader)

#made dictionairy -> convert to database
interests_database = {}
#all database things
veterans = {}
id = 1
for row in csv_reader:
    veterans[id] = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
    id += 1
