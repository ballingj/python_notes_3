"""
pip install pycodestyle
run:
pycodestyle <file_name>.py
"""

"""
# Original bad_styles code

import random, os

catString = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--, --Henry--, --Mr.Paws--"
def RANDOM_CAT(string_list):
    cat_list = catString.split(', ')# split the cats
    cat_list = [cat.strip('--') for cat in cat_list]
        return random.choice(cat_list)

print(  f'{RANDOM_CAT(catString)} is a good kitty'  )
"""

import random
import os

catString = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--, --Henry--, --Mr.Paws--"


def random_cat(string_list):
    cat_list = catString.split(', ')  # split the cats
    cat_list = [cat.strip('--') for cat in cat_list]
    return random.choice(cat_list)


print(f'{random_cat(catString)} is a good kitty')


""" 
Printing multiline text: this is called implied (or implicit) line "
continuation and it is the preferred approach for wrapping long lines, "
as you can read in the PEP-8 section on maximum line length.
"""

story = ("Once upon a time there was a very long string that was "
         "over 100 characters long and could not all fit on the "
         "screen at once.")

print(story)
