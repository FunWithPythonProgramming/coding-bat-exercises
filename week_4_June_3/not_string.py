"""Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

def not_string(a_string):
    if a_string[:3] == 'not':
        return a_string
    else:
        return "not " + a_string
