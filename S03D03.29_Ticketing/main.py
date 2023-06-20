print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
if height >= 120:
  print ("Yup")
  age = int(input("What is your age in years?"))
  if age < 12:
    print ("$5")
  elif age < 18:
    print("$7")
  else:
    print("$12")  
else:
  print ("Not So Yup")
  print ("extra")