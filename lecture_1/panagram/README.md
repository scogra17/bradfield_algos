# Polya's Method

## 1. Understand the Problem
* Show that a string contains 26 distinct, uniformly-cased alpha characters

## 2. Devise a Plan
1) a. Initialize a dictionary containing all 26 lower-cased letters as keys and 0 as value
b. Iterate over string, lower case each char and ~~add~~ set value to 1 if key exists
c. ~~Iterate over dictionary ensuring that all values > 0~~ Ensure sum of values is 26

2) a. Iterate over string and lower case each char
b. If the char is a letter (use regex or ASCII), add to a set
c. Check the length of the set to ensure it's 26

3) a. Use very long regex

## 3. Carry out the plan
See `panagram[1-3].py`

### How to run
Run from the command line, specifying an input string to test, e.g.:
```
./panagram1.py "the quick brown fox jumps over the lazy dog"
```

## 4. Review/extend