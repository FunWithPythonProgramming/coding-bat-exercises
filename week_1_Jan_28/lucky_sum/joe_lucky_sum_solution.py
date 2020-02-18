## gentsch coding bat homwork 2/2/2020

##Given 3 int values, abc,return their sum.However,if one of the values is 13 then it does not count towards the sum and values to its right do not count.
##So for example, if b is 13, then both b and c do not count.,


def lucky_sum(a, b, c):
    sum = 0
    if a == 13:
        sum = 0
    elif b == 13:
        sum = a
    elif a != 13 and b != 13 and c == 13:
        sum = (a + b)
    elif a != 13 and b != 13:
        sum = (a + b + c)
    return sum

    print(lucky_sum(1, 2, 3))  ##→ 6
    print(lucky_sum(1, 2, 13))  ##→ 3
    print(lucky_sum(1, 13, 3))  ##→ 1
    print(lucky_sum(1, 13, 13))  ##→ 1
    print(lucky_sum(6, 5, 2))  ##→ 13
    print(lucky_sum(13, 2, 3))  ##→ 0
    print(lucky_sum(13, 2, 13))  ##→ 0
    print(lucky_sum(13, 13, 2))  ##→ 0
    print(lucky_sum(9, 4, 13))  ##→ 13
    print(lucky_sum(8, 13, 2))  ##→ 8
    print(lucky_sum(7, 2, 1))  ##→ 10
    print(lucky_sum(3, 3, 13))  ##→ 6


# https://codingbat.com/prob/p107863"
