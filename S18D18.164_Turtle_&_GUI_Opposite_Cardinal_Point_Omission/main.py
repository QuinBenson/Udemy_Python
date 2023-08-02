import random
# AI Suggestion
def get_random_int_excluding_previous(previous_choice):
    random_choice = random.randint(0, 3)
    
    while random_choice == previous_choice:
        random_choice = random.randint(0, 3)
    
    previous_choice = random_choice
    return random_choice, previous_choice
  
#tuple of choices, just for the fun of tuples
tuple_opposite_list=(2,3,0,1)

# list when I was considering implementing
# double-ended list functionality to allow .rotate(-2)
# use:
# 'from collections import deque'
# https://www.geeksforgeeks.org/deque-in-python/
#tuple_list=(0,1,2,3)

# Attempt 01
#list of choices excluding the 'opposite' of the current choice
list_of_lists = [[0,1,3],[0,1,2],[1,2,3],[0,2,3]]
def hardcode_exclusion(previous_choice):
  random_choice = random.randint(0, 2)
  
  choice = list_of_lists[previous_choice][random_choice]
  return choice

# Attempt 01
def dynamic_exclusion(previous_choice):
  
  dynamic_list = list(tuple_opposite_list)
  dynamic_list.pop(previous_choice)
  
  # THIS DOES NOT PERFORM AS HOPED.
  # POP RETURNS THE VALUE REMOVED; THIS SUPERCEDES 
  # THE list() FUNCTION OUTPUT.
  # The exercise is possible but
  # the code becomes silly-complicated
  #dynamic_list=[list(tuple_list).pop (previous_choice)]


  
  choice = dynamic_list[random.randint(0, 2)]

  return choice
  
# # AI Suggestion Example usage:
# previous_choice = -1  # Initialize with a value that is not in the range 0 through 3
# random_choice, previous_choice = get_random_int_excluding_previous(previous_choice)
# # print("Random Choice:", random_choice)


# Testing Attempt 02
previous=random.randint(0, 2)
for _ in range(1,22):
  current=dynamic_exclusion(previous)
  print (f"{previous, current}")
  previous=current