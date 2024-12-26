"""Thhis module will test some functions
"""
from Sample_project.numbers import is_even
def test_is_even_or_not():
    """Testing the num is even or not

    Args:
        number (int): Checking the number
    """
    assert is_even(2) == True ,"2 is a even number"
def test_is_even_or():
    """Testing the num is even or not

    Args:
        number (int): Checking the number
    """
    assert is_even(3) == True ,"3 is a odd number"
   