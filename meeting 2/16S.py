# friend_1 = "Wendi"
# friend_2 = "Jenifer"
# friend_3 = "Cyntia"
# friend_4 = "Jhoni"
# friend_5 = "Jhon"


friends = ["Wendi", "Jenifer", "Cyntia", "Jhoni", "Jhon"]
friends[2] = "Taylor"
# friends[5] = "Jessica"
friends.append("Jessica")
# friends.remove("Jhoni")
# remove list based on index (index no 2)
#
# friends.remove("Wendi") # remove list based on value
friends.append("Emma")
# friends.pop(3) # remove list based on index
# print(friends)
# print(friends[:2])
# print(friends[:4])
# print(friends[2:5])

# programming_language = ("Python", "Java", "C++", "C#")
# programming_language[2] = "PHP"
# print(programming_language[1])

# Dictionary
#


data_movie = {
    'id' : 1,
    'name' : 'Harry Potter',
    'year' : 2005,
    'genre' : 'Fantasy',
    'rating' : 8.1,
    'director' : 'David Yates',
    'writer' : 'J.K. Rowling',
}


# print(data_movie)

data_movie['genre'] = "Horror"

print(data_movie['name'])
print(data_movie['genre'])
print(data_movie['director'])
