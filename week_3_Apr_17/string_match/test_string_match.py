from ron_solution import string_match
import pytest

@pytest.mark.parametrize(
    "string_a,string_b,expected",
    [('xxcaazz', 'xxbaaz', 3), ('xxcaazz', 'asdfgh', 0), ('xxcaazz', 'xxcaazz', 6),('', 'xxcaazz',0)],
)
def test_functional(string_a, string_b, expected):
    assert string_match(string_a, string_b) == expected