'''
Problem:
*In array of length x denoting sales quantities per minute in the week
*Receive list of lists with index of sums
*Input is integers

Approach 1
*Brute force - nested loop

Approach 2
*Slicing
*Iterate over queries and use values to slice sales array. Add values in sliced sales array and append to list to be returned
'''

def tshirt_sales1(sales, queries):
  sales_sums = []
  for idx, val in enumerate(queries):
    sales_values = sales[val[0]:val[1] + 1]
    sales_sum = sum(sales_values)
    sales_sums.append(sales_sum)
  return sales_sums

if __name__ == "__main__":
  # expected output [10, 3, 9]
  output1 = tshirt_sales1([1, 2, 3, 4], [[0, 3], [0, 1], [1, 3]])
  print(output1)


