from close_far import close_far

"""
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
while the other is "far", differing from both other values by 2 or more.

Note: abs(num) computes the absolute value of a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
"""

def test_close_far_positive_case():
    assert close_far(1, 2, 10)

def test_close_far_negative_case():
    assert not close_far(1, 2, 3)
