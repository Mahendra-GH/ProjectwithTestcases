"""This module test and produce the test cases
"""
from code.primeornot import is_prime
def test_is_prime_basic():
    
    assert not is_prime(0),"0 is a not prime"
    assert not is_prime(1),"1 is a not prime"
    assert not is_prime(-3),"Negitive is a not prime"
    assert not is_prime(4),"7 is a not prime"
    assert is_prime(7),"7 is a prime"
    
    
    