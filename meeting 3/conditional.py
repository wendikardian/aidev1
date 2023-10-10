allowance = 10
spending = 8

# print(allowance > spending)
# print(allowance < spending)
# print(allowance != spending)
# print(allowance == spending)
# print((allowance == spending) and (allowance > spending))


students_name = ['Alex', 'Bryan', 'Christ', 'Dave', 'Eva']
students_score = [89, 100, 76, 79, 80]
students_grade = [] 

for i in students_score : 
    if(i >= 90):
        students_grade.append("A")
    elif( i >= 80):
        students_grade.append("B")
    else: 
        students_grade.append("C")
    

print(students_grade)