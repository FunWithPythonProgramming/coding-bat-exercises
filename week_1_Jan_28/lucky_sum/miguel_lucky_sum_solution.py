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