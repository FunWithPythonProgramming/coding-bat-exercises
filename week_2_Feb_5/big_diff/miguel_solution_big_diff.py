# Dev: Miguel Rovira-Gonzalez
# Date: 2/11/2020
# Homework: codingbat big diff python problem, https://codingbat.com/prob/p184853
# Problem to solve:
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
# Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8


def big_diff(*args):
    """
    param: *args (this is a list of arguments, it can be unknown which is why you use *args
    purpose: the purpose of this function is to find the highest and lowest value in an array of integers and subtract the differece between them
    return highest_value - lowest_value
    """
    highest_value = max(*args)
    lowest_value = min(*args)
    return highest_value - lowest_value

# Unit Testing Function


print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))
