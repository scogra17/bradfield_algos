#!/usr/local/bin/python3

import string
import argparse
import re

# Use the first argument as the input string to be tested
my_parser = argparse.ArgumentParser(description='Determine if a string is a panagram')
my_parser.add_argument('String', type=str, help='the string to analyze')
args = my_parser.parse_args()
potential_panagram = args.String

def is_panagram(sentence):
  found_lower_letters = set()
  for letter in sentence:
    if re.match("[a-z]", letter.lower()):
      found_lower_letters.add(letter.lower())
  if len(found_lower_letters) == 26:
    return True
  return False


print("Is panagram? " + str(is_panagram(potential_panagram)))