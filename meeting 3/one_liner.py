name = ['josh', 'james', 'joe', 'jim']
# for i in name:
#     print(i)
 
# for one liner saperate it with enter
# [print(i) for i in name]
# one liner



# for i in range(1,2,1):
#     print(name[i])

# [print(name[i]) for i in range(1,2,1)]

# score = 90
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# else:
#     print('C')
 
# one liner
# print('A') if score >= 90 else print('B') if score >= 80 else print('C')

students_name = ['Alex','Bryan','Christ','Dave ','Eva']
students_score = [100,75,80,78,99]
students_grade = []
students_grade = ['A' if i >= 90 else
                   'B' if i >= 70 else
                     'C' 
                     for i in students_score]; 
print(students_grade)

# example while loop one liner
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# one liner of that while loop (using while)
# i = 0
# while i < 10: print(i); i += 1

