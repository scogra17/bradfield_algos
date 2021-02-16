#!/usr/local/bin/python3

import string
import argparse

# Use the first argument as the input string to be tested
my_parser = argparse.ArgumentParser(description='Determine if a string is a panagram')
my_parser.add_argument('String', type=str, help='the string to analyze')
args = my_parser.parse_args()
potential_panagram = args.String

def is_panagram(sentence):
  # Create dictionary of all lower case letters
  all_lower_letters = dict.fromkeys(string.ascii_lowercase, 0)

  for letter in sentence:
    if letter.lower() in all_lower_letters:
      all_lower_letters[letter.lower()] = 1
  if sum(list(all_lower_letters.values())) == 26:
    return True
  return False

print("Is panagram? " + str(is_panagram(potential_panagram)))