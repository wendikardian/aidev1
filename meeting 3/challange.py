import random

names = []

print("Add name to shuffle \n press 'S' to Stop " )
while True:
    add_name = input("add name : ")
    if add_name.lower() != 's':
        names.append( add_name )
    else:
        random_name = random.choice( names )
        print("Choosen person : " + random_name) 
        break;