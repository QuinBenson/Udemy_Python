rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
#ASCII art into an array
l_pretty_output = [rock, paper, scissors]

#the list of choices available
l_computer_choice = ["R", "P", "S"]

#lists showing win/lose alternatives
#offset 0 is beating option, offset 1 is losing option
l_R = ["P", "S"]
l_P = ["S", "R"]
l_S = ["R", "P"]

#win lose alternatives into 2D array
l_win_lose = [l_R, l_P, l_S]

#computer's pick
l_random = random.randint(0, 2)

#user's pick
l_user_choice = input("R,P,S ").upper()

#find offset posn of user's pick in the list of possible choices
l_user_offset = l_computer_choice.index(l_user_choice)

#Display The Pretty Bits Here
print(l_pretty_output[l_user_offset] + "\n" + l_pretty_output[l_random])

#bit inconsistent, but if equal choices, then it's a draw
if l_user_choice == l_computer_choice[l_random]:
    print("Draw")

#if user choice matches winning option against computer
# user wins
elif l_win_lose[l_random][0] == l_user_choice:
    print("You Win")
#if user choice matches losing option against computer
# user loses
elif l_win_lose[l_random][1] == l_user_choice:
    print("You Lose")
else:
    #currently not reached
    print("You What?")
