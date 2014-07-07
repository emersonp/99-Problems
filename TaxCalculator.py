# Copyright (C) 2014 Parker Harris Emerson
# From https://github.com/karan/Projects

print("\n" * 100)
print("Welcome to Parker's Simplest Tax Calculator (TM).")
base_cost = float(input("How much does the thing cost? $"))
tax = float(input("What percent tax are you paying? %"))
total_cost = base_cost * (1 + tax / 100)
total_cost = format(total_cost, ',.2f')
print("You will have to pay $" + str(total_cost), "including tax.")
