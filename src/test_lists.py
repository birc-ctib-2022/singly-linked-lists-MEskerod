"""List tests."""

from lists import (Link, length, drop, take, reverse)


def test_length(): 
    assert length(None) == 0
    assert length(Link(1, Link(2, Link(3, Link(4, None))))) == 4
    assert length(Link(1, Link(4, None))) == 2  


def test_drop(): 
    assert drop(None, 4) == None
    assert drop(Link(5, Link(3, Link(1, None))), 5) == None
    assert drop(Link(5, Link(3, Link(1, None))), 2) == Link(1, None)
    assert drop(Link(5, Link(3, Link(1, None))), 0) == Link(5, Link(3, Link(1, None)))


def test_take(): 
    assert take(None, 4) == None 
    assert take(Link(1, Link(5, Link(7, None))), 8) == Link(1, Link(5, Link(7, None)))
    assert take(Link(1, Link(4, Link(10, None))), 1) == Link(1, None) 


def test_reverse():
    assert reverse(None) == None
    assert reverse(Link(4, None)) == Link(4, None)
    assert reverse(Link(5, Link(1, Link(9, Link(2, None))))) == Link(2, Link(9, Link(1, Link(5, None))))