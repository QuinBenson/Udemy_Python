# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# -1 accounts for offset indexing
#l_player_count=len(names)-1
#l_offset=random.randint(0,l_player_count)
# print (names[l_offset] + " is going to buy the meal today!")

print (names[random.randint(0,len(names)-1)] + " is going to buy the meal today!")