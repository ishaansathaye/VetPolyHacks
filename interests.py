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

def make_common_interests_dict(user_id, interests_database):
    user_interest_dict = {}
    for interest in veterans[user_id].interests:
        for user in interests_database[interest]:
            if user != user_id:
                if user not in user_interest_dict:
                    user_interest_dict[user] = 1
                else:
                    user_interest_dict[user] += 1
    return determine_common_users(user_interest_dict)
    
def determine_common_users(interestDict):
    common_users = []
    for user in interestDict:
        if interestDict[user] >= 4:
            common_users.append(user)
    return common_users

current_user = 'JB1994'
interests_database = initialize_interest_dict(veterans)
final_interests = make_common_interests_dict(current_user, interests_database)
for user_id in final_interests:
    final_list = ", ".join(list(set(veterans[current_user].interests) & set(veterans[user_id].interests))).lower()
    print("You and", veterans[user_id].first, veterans[user_id].last, "have interests like", final_list, "or more in common.")
