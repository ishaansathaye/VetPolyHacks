import csv
from math import radians, cos, sin, asin, sqrt

file = open('mockdatabase.csv')
csv_reader = csv.reader(file)
header = next(csv_reader)

class Person():
    def __init__(self, id, first, last, branch, role, f_year, l_year, meet, age, interests, zip, max_radius, lat, longitude):
        self.id = id
        self.first = first
        self.last = last
        self.branch = branch
        self.role = role
        self.f_year = int(f_year)
        self.l_year = int(l_year)
        self.meet = bool(meet)
        self.age = int(age)
        self.interests = interests.split(", ")
        self.zip = zip
        self.max_rad = float(max_radius)
        self.lat = lat
        self.longitude = longitude

#calculates the distance between an inputted latitude and longitude and the latitude and longitude of the person object
def __calculate_distance__(otherlat, otherlong):
    lat, longitude, otherlat, otherlong = map(radians, [lat, longitude, otherlat, otherlong])
    # haversine formula
    dlon = otherlong - longitude
    dlat = otherlat - lat
    a = sin(dlat/2)**2 + cos(lat) * cos(otherlat) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 3956.09
    return c * r

#sample
# row = next(csv_reader)
# sample_person = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
# print(sample_person.interests)
