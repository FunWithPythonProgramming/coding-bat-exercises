
def has22(nums):
  int_array_count = len(nums)
  for x in range(int_array_count -1):
    if nums[x] == 2 and nums[x] == nums[x +1]:
      return True
  return False

print(has22([1, 2, 2])) #→ True
print(has22([1, 2, 1, 2]))# → False
print(has22([2, 1, 2]))# → False
print(has22([2, 2, 1, 2]))# → True
print(has22([1, 3, 2])) #→ False
print(has22([1, 3, 2, 2])) #→ True
print(has22([2, 3, 2, 2])) #→ True
print(has22([4, 2, 4, 2, 2, 5]))# → True
print(has22([1, 2])) #→ False
print(has22([2, 2]))# → True
print(has22([2])) #→ False
print(has22([])) #→ False
print(has22([3, 3, 2, 2])) #→ True
print(has22([5, 2, 5, 2]))#→ False



#https://codingbat.com/prob/p119308