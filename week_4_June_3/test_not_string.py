from not_string import not_string
import pytest

"""Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

def test_not_added_to_beginning():
    assert not_string('candy') == 'not candy'

def test_already_starts_with_not():
    assert not_string('not candy') == 'not candy'
