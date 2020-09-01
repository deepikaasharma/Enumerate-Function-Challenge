"""Write a function called alt_series. This function should have one parameter which will be a list of numbers. This function should:

    In a variable called alt_sum, sum together all the numbers in num_list where the values with even indices are added and the values with odd indices are subtracted
    In a variable called pow_sum, sum together the result of raising each value to the power of its index
    In a variable called idx_sum, sum together the result of raising each index to the power of the value at that index

The function should return these three variables in the order alt_sum, pow_sum, idx_sum.

Note:

    Recall that in order to return multiple values from a function, you can simply separate them with commas
    The summation index should start at 1

Example:

    alt_series([2, 4, 6, 8]) -> (4, 4330, 66282)
    alt_series([1, 1, 1, 1]) -> (0, 4, 10)

"""

num_lst = [2, 4, 6, 8]


def alt_series(num_lst):
  alt_sum = 0
  pow_sum = 0
  idx_sum = 0
  
  for idx, val in enumerate(num_lst,1):
    
    if idx%2==0:
      alt_sum += val
    else: 
      alt_sum -=val

  for idx, val in enumerate(num_lst, 1):
    pow_sum += (val**idx)
  

  for idx, val in enumerate(num_lst, 1):
    idx_sum += (idx**val)
  #   idx_sum.summation(idx**val)
  
  return alt_sum, pow_sum, idx_sum

print(alt_series([2, 4, 6, 8]))

    

    
 