def rotate_left3(nums):
  first_num = nums[0]
  for index in range(1,3):
    nums[index-1] = nums[index]
  nums[2] = first_num
  
  return nums
