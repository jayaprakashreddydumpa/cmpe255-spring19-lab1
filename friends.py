#!/usr/bin/env python
# coding: utf-8

# In[5]:


import operator
users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

''' Creating a new dictionary to '''
friendship_list = {}

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    num_friends = 0
    for i,x in enumerate(users):
        if user == users[i]['name']:
            user_id = users[i]['id']
            for j,y in enumerate(friendship):
                if (user_id == friendship[j][0]) | (user_id == friendship[j][1]):
                    num_friends = num_friends + 1
            friendship_list.update({users[i]['name']:num_friends})
    pass

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
#     sorted_list = {}
#     for elem in sorted(friendship_list.values()):
#         sorted_list.update({elem[0]:elem[1]})
#     print(sorted_list)
    sorted_x = sorted(friendship_list.items(), key=operator.itemgetter(1), reverse= True)
    for i in sorted_x:
        print(i)
    pass

for user in users:
    num_friends(user['name'])

print("Number of friends for each user")
print(friendship_list)

print("\nSorted list of users based on number of friends")
sort_by_num_friends()





