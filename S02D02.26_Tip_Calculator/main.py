#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
l_bill=float(input("What's the damage? "))
l_people=int(input("how many bodies? "))
l_percentage = float(input("percentage? "))
l_perhead= round(l_bill*((100+l_percentage)/100)/l_people,2)
print(f"That'll be {l_perhead:3.2f}")