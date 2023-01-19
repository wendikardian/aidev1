import random

subjects = ("Python", "C++", "Javascript")
print(subjects)
print(len(subjects))

print(subjects[-1])
print(subjects[1])
print(subjects[0: 2])

print("Python" in subjects)
print("Java" in subjects)


# Unpack the tuples 
s1, s2, s3 = subjects

print(s1)
print(s2)
print(s3)


my_fav = random.choice(subjects)

random_num = random.randint(0, 2)

print(my_fav)
print(subjects[random_num])