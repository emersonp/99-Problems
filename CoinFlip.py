# Copyright (c) 2014 Parker Harris Emerson
# From https://github.com/karan/Projects

import random

coin_flips = 0
heads = 0
tails = 0
print("\n" * 100)
print("Welcome to Parker's Coin Flip Simulator (TM)! ")
user_flips = int(input("How many times would you like to flip the coin? "))

while coin_flips < user_flips:
  flip = random.randrange(2)
  if flip == 0: heads+= 1
  else: tails += 1
  coin_flips += 1

print ("Coin flipped", coin_flips, "times.")
print ("Heads:", heads, "/ Tails:", tails)
