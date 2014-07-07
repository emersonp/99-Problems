# Copyright (C) 2014 Parker Harris Emerson
# From https://github.com/karan/Projects

print("\n" * 100)
print("Welcome to Parker's Tile Floor Cost Calculator (TM).")
tile_cost = float(input("How much does your tile cost per square foot? $"))
tile_width = float(input("How wide an area are you covering (in feet)? "))
tile_height = float(input("How high an area are you covering (in feet)? "))
total_cost = format(tile_cost * tile_height * tile_width, ',.2f')
print("You will have to spend $" + str(total_cost), "for tile.")
