import random
import string


print("Welcome to Password maker !")

abjectives_list = ["Sleepy", "Slow", "Fluffy", "Red", "Yellow", "Hard", "Soft", "Nice"]
nouns_list = ["Mug", "Potato", "Chair", "Mouse", "Dragon", "Hammer", "Tablet"]

abjective =random.choice(abjectives_list)
noun = random.choice(nouns_list)
number = random.randrange(0, 100)
char = random.choice(string.punctuation)


password =abjective + noun + str(number) + char 

print("Your new Password is : " + password)