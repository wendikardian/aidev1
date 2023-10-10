#  List grocery items
grocery_list = ["milk", "eggs", "bread", "cheese", "butter", "apples", "bananas", "grapes", "oranges", "strawberries",
                "blueberries", "raspberries", "blackberries", "chicken", "beef", "pork", "fish", "shrimp", "rice", ]
# print(grocery_list[0])
# print(grocery_list[1])
# print(grocery_list[2])
# print(grocery_list[3])
# print(grocery_list[4])

# for item in grocery_list:
#     print(item)
#     print("Hello World")

# for i in range(1, 10, 2):
#     print(i)

# for i in range(5):
#     print(i)
#     # print("Hello World ! ")
#     for j in range(3):
#         print(j)
#         print("Hello world")


grade = 100
min_grade = 95

# print(grade != min_grade)

# if grade < min_grade:
#     print("You failed the class")
# else:
#     print("You passed the class")


# grade = 93

# if grade > 90:
#     if grade > 95:
#         print("Nice")
#     else:
#         print("A")
#     print("A+")
# elif grade > 80:
#     if grade > 85:
#         print("B+")
#     else:
#         print("B")
# elif grade > 70:
#     print("C")
# else:
#     print("D")


# while True:
#     answer = input("quit or not ")
#     if answer.lower() == "quit":
#         break
#     else:
#         print("Hello World")


# names = ['Cleo', 'Wendi', 'James', 'Jeniffer', 'David', 'George', 'Thompson']

# for name in names:
#     print(name)

# using one liner
# [print(name) for name in names]

# score = 90
# if score  >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# else:
#     print("C")

# using one liner
score = 90
print("A") if score >= 90 else print("B") if score >= 80 else print("C")
