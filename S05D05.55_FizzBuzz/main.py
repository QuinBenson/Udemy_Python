#Write your code below this row 👇
#FizzBuzz 1 to 100

for x in range(1, 101):
  #set printout string to zero length  
  l_str = ""
  #test if current iteration is divisible by 3; if yes, append fizz to printout string
  if x % 3 == 0:
    l_str += "Fizz"

#test if current iteration is divisible by 5; if yes, append fizz to printout string
  if x % 5 == 0:
    l_str += "Buzz"

#if neither fizz, buzz nor fizzbuzz, set printout string to number of current iteration
  if len(l_str) == 0:
    l_str = str(x)
  
  print(l_str)

