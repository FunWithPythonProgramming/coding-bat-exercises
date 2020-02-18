"""
We want to make a row of bricks that is goal inches long. We have a number 
of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. 
See also: Introduction to MakeBricks


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True

"""


def make_bricks(small, big, goal):

    first = small * 1
    second = big * 5
    
    if (first + second) == goal:
        return True
    elif small == (goal - second):
        return True
    elif second == goal:
        return True
    elif goal % 5 == (second % 5) + small:
        return True
    else:
        return False
    
print(make_bricks(3, 1, 8)) # Expects True
print(make_bricks(3, 1, 9)) # Expects False
print(make_bricks(3, 2, 10)) # Expects True
print(make_bricks(3, 2, 8)) # Expect True
print(make_bricks(3, 2, 9)) # Expects False
print(make_bricks(3, 2, 9)) # Expects → False
print(make_bricks(1, 4, 11)) # Expects True
print(make_bricks(0, 3, 10)) # Expects True
