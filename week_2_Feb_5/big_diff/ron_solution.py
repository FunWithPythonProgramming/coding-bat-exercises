def big_diff(nums):
  current_min = nums[0]
  current_max = nums[0]
  for number in nums[1:]:
    current_min = min(current_min, number)
    current_max = max(current_max, number)
  return current_max - current_min
