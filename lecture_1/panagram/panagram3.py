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
  # Build regex pattern using positive lookaheads
  # i.e. ^(?=.*a)(?=.*b)...(?=.*z).+
  pattern = "^"
  for letter in string.ascii_lowercase:
    pattern += "(?=.*{0})".format(letter)
  pattern += ".+"

  if re.match(pattern, sentence.lower()):
    return True
  return False


print("Is panagram? " + str(is_panagram(potential_panagram)))