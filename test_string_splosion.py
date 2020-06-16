from g_kim_string_splosion import string_splosion
import pytest

def test_string_splosion():
    assert string_splosion('Code') == 'CCoCodCode'
    assert string_splosion('abc') == 'aababc'
    assert string_splosion('ab') == 'aab'
    assert string_splosion('x') == 'x'
    assert string_splosion('fade') == 'ffafadfade'
    assert string_splosion('There') == 'TThTheTherThere'
    assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
    assert string_splosion('Bye') == 'BByBye'
    assert string_splosion('Good') == 'GGoGooGood'
    assert string_splosion('Bad') == 'BBaBad'