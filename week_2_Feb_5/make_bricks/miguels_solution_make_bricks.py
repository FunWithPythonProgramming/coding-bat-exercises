# Dev: Miguel Rovira-Gonzalez
# Date: 2/11/2020
# Homework: codingbat make bricks python problem, https://codingbat.com/prob/p118406
# Problem to solve:
#----------------------------------------------------------------------------------------
# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from the given bricks.
# This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

"""
make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
"""

def make_bricks(small_brick, big_brick, goal):
    # one small brick = 1 inch, so 3 small would be 3 inches
    # one big brick would be 5 inches so two big bricks would be 10 inches
    # you don't have to use all the bricks
    small = 1
    big = 5

    if (small_brick * small) + (big_brick * big) == goal:
        return True

    elif (small_brick * small) == goal:
        return True

    elif (big_brick * big) == goal:
        return True

    elif (big_brick * big) % big_brick == 0:
        big_brick = big
        if (small_brick * small) + big_brick == goal:
            return True

        elif (small_brick * small) + (big_brick * 2) == goal:
            return True

        elif (small_brick * small) + (big_brick * 1) == goal:
            return True

    else:
        return False

# print(make_bricks(3, 1, 8)) # Expects True
# print(make_bricks(3, 1, 9)) # Expects False
# print(make_bricks(3, 2, 10)) # Expects True
# print(make_bricks(3, 2, 8)) # Expect True
# print(make_bricks(3, 2, 9)) # Expects False
# print(make_bricks(3, 2, 9)) # Expects → False
# print(make_bricks(1, 4, 11)) # Expects True
# print(make_bricks(0, 3, 10)) # Expects True

print(make_bricks(3, 1, 7)) # Expects  True
# make_bricks(1, 1, 7) → False	False	OK
# make_bricks(2, 1, 7) → True	True	OK
# make_bricks(7, 1, 11) → True	False	X
# make_bricks(7, 1, 8) → True	False	X
# make_bricks(7, 1, 13) → False	False	OK
# make_bricks(43, 1, 46) → True	False	X
# make_bricks(40, 1, 46) → False	False	OK
# make_bricks(40, 2, 47) → True	False	X
# make_bricks(40, 2, 50) → True	True	OK
# make_bricks(40, 2, 52) → False	False	OK
# make_bricks(22, 2, 33) → False	False	OK
# make_bricks(0, 2, 10) → True	True	OK
# make_bricks(1000000, 1000, 1000100) → True	False	X
# make_bricks(2, 1000000, 100003) → False	False	OK
# make_bricks(20, 0, 19) → True	False	X
# make_bricks(20, 0, 21) → False	False	OK
# make_bricks(20, 4, 51) → False	False	OK
# make_bricks(20, 4, 39) → True	False	X
# other tests
# 		X

