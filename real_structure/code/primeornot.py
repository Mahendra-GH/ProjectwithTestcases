"""primeornot.py
this module tells if the number is prime or not
"""
def is_prime(number):
    """This function returns prime if the number % index!=0

    Args:
        number (int): number to be check

    Returns:
        prime_number(int): returns prime if the number % index!=0
    """
    is_prime_number = True
    if number<=1:
        is_prime_number = False
    for index in range(2,number):
        if number%index==0:
            is_prime_number = False
            break
    return is_prime_number
               

            
            
   
