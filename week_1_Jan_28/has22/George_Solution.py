"""Given an array of ints, return True if the array contains a 2 next to a 2 somewhere."""


def has22(nums):
  
  #next = len(nums)
  #two_counter = 0
  
  #for x in range(next):
    #if nums[x] == 2 and nums[x + 1] == 2:
     # return True

    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True

    return False