from person import Person
from event import Event
import csv
import pandas as pd
import requests
from math import radians, cos, sin, asin, sqrt

def initialize_groups():
    df1 = pd.read_csv("mockdatabase.csv")
    df2 = pd.read_csv("latlong.csv")
    df3 = pd.merge(df1, df2, on="ZIP")
    df3.to_csv("database_to_use.csv", index=False)
    file = open('database_to_use.csv')
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    #all database things
    veterans = {}
    id = 1
    for row in csv_reader:
        veterans[row[0]] = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
        id += 1
    return veterans

#calculates the distance between an inputted latitude and longitude and the latitude and longitude of the person object
def calculate_distance(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    # haversine formula
    dlat = lat1 - lat2
    dlon = long1 - long2
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 3956.09
    return c * r

def find_closest_events():
    vets = initialize_groups()
    testing_user_id = "AN1987"
    user = vets[testing_user_id]
    df = pd.read_csv("events.csv")
    print(user)
    #df5 = pd.merge(df4, df3, on="ZIP")
    #df5.to_csv("test.csv", index=False)
    events = {}
    final_events = {}
    for i in range(len(df["LAT"].index)):
        lat = df["LAT"][i]
        long = df['LONG'][i]
        event_distance = calculate_distance(user.lat, user.longitude, lat, long)
        events[event_distance] = Event(df["Name"][i], df["ZIP"][i], df["LAT"][i], df["LONG"][i])
        distances = list(events.keys())
        distances.sort()
    for key in distances:
        final_events[key] = events[key]

    print(final_events[list(final_events.keys())[0]].name)

find_closest_events()
