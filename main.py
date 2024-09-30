# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

#generates a random integer, either 0 or 1
random_number = random.randint(0, 1)
#now the code prints heads or tails
if random_number == 1:
  print("Heads")
else:
  print("Tails")
