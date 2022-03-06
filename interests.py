from person import Person
import csv
file = open('mockdatabase.csv')
csv_reader = csv.reader(file)
header = next(csv_reader)

#creates people objects for all in our database
veterans = {}
for row in csv_reader:
    veterans[row[0]] = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])

#puts all people that share interests in a dictionary
def initialize_interest_dict(veteranObjDict):
    interests_database = {}
    for veteran_id in veteranObjDict:
        for interest in veteranObjDict[veteran_id].interests:
            if interest in interests_database:
                interests_database[interest].append(veteran_id)
            else:
                interests_database[interest] = [veteran_id]
    return interests_database

def find_interests_connections(user_id, interests_database):
    user_interest_dict = {}
    for interest in veterans[user_id].interests:
        for user in interests_database[interest]:
            if user != user_id:
                if user not in user_interest_dict:
                    user_interest_dict[user] = 1
                else:
                    user_interest_dict[]

interest_dict = initialize_interest_dict(veterans)
print([key for key in interest_dict])
    
