# Dev: Miguel Rovira-Gonzalez

# Coding Bat Exercise 1
# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
"""
array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""
def array_front9(data_parameters):
    if 9 in data_parameters[:4]:
        return True
    else:
        return False

array_front9([1, 2, 9, 3, 4])
array_front9([1, 2, 3, 4, 9])
array_front9([1, 2, 3, 4, 5])

# Coding Bat Exercise 2
# Given 3 int values, a b c, return their sum.
# However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
"""
lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
"""

def lucky_sum(int_one, int_two, int_three):
    if int_one == 13:
        return 0
    elif int_two == 13:
        return int_one
    elif int_three == 13:
        return int_one + int_two
    else:
        return int_one + int_two + int_three

lucky_sum(1, 2, 3) # 6
lucky_sum(1, 2, 13) # 3
lucky_sum(1, 13, 3) # 1

# Coding Bat Exercise 3
# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
"""
has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""
def has22(numbers):
    for number in numbers:
        if numbers[number] == 2 and numbers[number + 1] == 2:
            return True
    return False

print(has22([1, 2, 2, 2]))
