# Define a list and access it

grocery_list = ["Bread", "Cereal", "Milk", "Sauce", "Fruit"]
print(grocery_list)
print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[-1])

# Add and remove the data
grocery_list.append("Juice")
grocery_list.append("Mango")
grocery_list.remove("Milk")

print(grocery_list)


# Change the data of the list

grocery_list[1] = "Strawberry Jam"
print(grocery_list)
print(len(grocery_list))


# Exercise JIO 

numbers = [130,100,140,150,190, 200, 250, 200, 230, 250]
print(numbers)

numbers.sort()
print(numbers)


# List slicing

grade_3 = numbers[:4]
grade_2 = numbers[4: 7]
grade_1 = numbers[7:]


print(grade_1)
print(grade_2)
print(grade_3)