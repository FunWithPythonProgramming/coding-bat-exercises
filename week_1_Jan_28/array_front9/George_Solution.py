
"""Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
The array length may be less than 4."""


def array_front9(nums):
  
  last = len(nums)
  
  if last > 4:
    last = 4
    
  for x in range(last):
    if nums[x] == 9:
      return True
  return False