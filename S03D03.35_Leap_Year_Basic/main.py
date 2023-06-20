# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    message = "Leap year."
    if year % 100 == 0:
        if year % 400 == 0:
            message = "Leap year."
        else:
            message = "Not leap year."
else:
    message = "Not leap year."
    
print (message)

