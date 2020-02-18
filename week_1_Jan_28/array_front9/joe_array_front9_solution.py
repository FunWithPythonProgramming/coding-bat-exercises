def array_front9(nums):
    end = len(nums)
    if end == 4:
        end = 4

    for index in range(end):
        if nums[index] == 9:
            return True
    return False

## https://codingbat.com/prob/p110166"
