#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

l_result = random.randint(0,1)

if l_result == 1:
    print("Heads")
elif l_result==0:
    print("Tails")
else:
    print("Buggerup")
    