l_TRUE_counter=0
l_LOVE_counter=0
l_str="bathmat" + "CANTANKER"
print (l_str)
l_str_lower=l_str.lower()
# for l_letter in l_str_lower:
for l_TRUE_letter in "true":
   l_TRUE_counter+=l_str_lower.count(l_TRUE_letter)
    # print (l_TRUE_letter, l_str_lower.count(l_TRUE_letter))
for l_LOVE_letter in "love":
  l_LOVE_counter+=l_str_lower.count(l_LOVE_letter)
print (f"{l_TRUE_counter}{l_LOVE_counter}")

#less than 10 or greater than 90
# ove Scores less than 10 or greater than 90, the message should be:
l_score_str=str(f"{l_TRUE_counter}{l_LOVE_counter}")
l_score=int(l_score_str)
l_message= "Your score is " + l_score_str

if l_score <=10 or l_score >= 90:
  l_message+=", you go together like coke and mentos."
if l_score >=40 and l_score <=50:
  l_message+=", you are alright together."

print(l_message)

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
