
import numpy as np

def harmonic_sum(last_term: int) -> float:
    """
    Compute the the harmonic sum
    
    Harmonic sum is defined as: 1 + 1/2 + 1/3 + ... + 1/last_term

    Args:
        last_term (int): The last term of the harmonic series

    Returns:
        float: The sum
    """
    
    sum_ = 0
    for i in range(1, last_term + 1):
        sum_ += 1 / i
    return sum_


def harmonic_sum_backwards(last_term: int) -> float:
    """
    Compute the the harmonic sum
    
    This fucntion is executed in reverse order 1/last_term + 1/(last_term - 1) + ... + 1

    Args:
        last_term (int): The last term of the harmonic series

    Returns:
        float: The sum
    """
    
    sum_ = 0
    for i in range(last_term, 0, -1):
        sum_ += 1 / i
    return sum_


# Rounding error
print("Round error")
print("22/5 should be equal to harmonic_sum(5) but the result is:", 22/5 == harmonic_sum(5))

print()

# Overflow error
print("Overflow error")
print("The harmonic sum of 10^6 raised to the power of 6969 should cause an overflow error:", end=" ")
try:    
    print(harmonic_sum(10**6)**6969)    
except OverflowError as e:
    print("overflow error occured", e)
    
    
print()


# Underflow error
print("Underflow error")
print("The harmonic sum of 10^6 raised to the power of -6969 should cause the result of 0.0:", end=" ")
try:
    print(harmonic_sum(10**6)**(-6969))
except ZeroDivisionError as e:
    print("underflow error occured", e)

print()

# violation of associativity
print("Associativity violation")
print("The harmonic sum of 10^6 is not equal to the harmonic sum of 10^6 in reverse order:", end=" ")
print(harmonic_sum_backwards(10**6) == harmonic_sum(10**6))
