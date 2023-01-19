friends_list = ["Amanda", "Bruno", "Camila", "Drake", "Elvis", "Freddie", "George", "Harry", "Iggy", "Joji"]

for friend in friends_list:
    print(friend)


print("=== only three ===")
for i in range(3):
    print(friends_list[i])


print("=== all of the friends")
for i in range(0, len(friends_list), 1):
    print(friends_list[i])


print("==== challange ====")

for i in range(3):
    print("Im am learning Python")

for i in range(5, 100, 5):
    print(i)