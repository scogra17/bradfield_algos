#!/usr/local/bin/python3

import stack as s 

def reverse_list(values):
	stack = s.Stack()
	for item in values: 
		stack.push(item)

	i = 0 
	while not stack.is_empty():
		values[i] = stack.pop()
		i = i + 1
	return values

print(reverse_list(["a","b","c"]))
