#Step 1
import random

fail_count = 0
fail_max= 12
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# OLD WAY
# chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word_len=len(chosen_word)
guessed_so_far_str = "–" * chosen_word_len
guessed_so_far_list = list(guessed_so_far_str)
print(guessed_so_far_str)
while (guessed_so_far_list.count("–") > 0 ) and fail_count<=fail_max:
  
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter ").lower()
    
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for checked_letter in range(chosen_word_len):
    
        if guess == chosen_word[checked_letter]:
          guessed_so_far_list[checked_letter] = guess
          
    if guessed_so_far_str == "".join(guessed_so_far_list):
      fail_count+=1
    else:
      guessed_so_far_str = "".join(guessed_so_far_list)
          
    print(guessed_so_far_str)
if fail_count <= fail_max:
  print ("WIN")
else:
  print ("LOSE")