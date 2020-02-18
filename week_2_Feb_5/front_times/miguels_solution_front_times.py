# Dev: Miguel Rovira-Gonzalez
# Date: 2/11/2020
# Homework: codingbat front times python problem, https://codingbat.com/prob/p165097
# Problem to solve:
# Given a string and a non-negative int n,
# we'll say that the front of the string is the first 3 chars
# or whatever is there if the string is less than length 3. Return n copies of the front;


def front_times(string, number=1):
    """
    porams (string, number)
    purpose: the purpose of this method is to take the first 3 characters in a string, and then have string returned by
    the multiplication of the number used as the argument
    # front_times('Chocolate', 2) → 'ChoCho'
    # front_times('Chocolate', 3) → 'ChoChoCho'
    # front_times('Abc', 3) → 'AbcAbcAbc'
    """
    return string[:3] * number

print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))
print(front_times("Mi", 2))
