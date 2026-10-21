import numpy as np

def fib(n: int) -> int:
    '''
    Test function to compute the nth Fibonacci number using matrix exponentiation.
    '''
    f = np.matrix([[1, 1], [1, 0]])
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    else:
        return (f ** (n - 1))[1, 0]