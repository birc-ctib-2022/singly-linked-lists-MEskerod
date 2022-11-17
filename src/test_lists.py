"""List tests."""

from lists import (Link, length, drop, take, reverse)


def test_length(): 
    assert length(None) == 0
    assert length(Link(1, Link(2, Link(3, Link(4, None))))) == 4
    assert length(Link(1, Link(4, None))) == 2  


def test_drop(): 
    assert drop(None, 4) == None


def test_take(): 
    assert take(None, 4) == None 


def test_reverse():
    assert reverse(None) == None