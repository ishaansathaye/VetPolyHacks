from person import Person
import csv
import pandas as pd
import requests

def initialize_groups():
    df1 = pd.read_csv("mockdatabase.csv")
    df2 = pd.read_csv("latlong.csv")
    df3 = pd.merge(df1, df2, on="ZIP")
    df3.to_csv("test.csv", index=False)
    file = open('mockdatabase.csv')
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    #all database things
    veterans = {}
    id = 1
    for row in csv_reader:
        df = pd.read_csv("latlong.csv")
        veterans[row[0]] = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
        id += 1

    return veterans

vets = initialize_groups()

events
