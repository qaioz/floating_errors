import numpy as np

def derivative_richardson_4(f, x, h):
    
    D_h = np.divide(np.subtract(f(x + h), f(x - h)), np.multiply(2, h))
    D_h2 = np.divide(np.subtract(f(x + h / 2), f(x - h / 2)), h)
    
    D = np.divide(np.subtract(np.multiply(4, D_h2), D_h), 3)
    return D


def derivative_richardson_2(f, x, h):
    D_h = np.divide(np.subtract(f(x + h), f(x - h)), np.multiply(2, h))
    
    return D_h


def derivative_richardson(f, x, h, h_ord):
    if h_ord == 2:
        return derivative_richardson_2(f, x, h)
    elif h_ord == 4:
        return derivative_richardson_4(f, x, h)
    else:
        raise ValueError("h_ord must be 2 or 4")

from typing import Callable

def newton_rhapson(
    f: Callable[[float], float], 
    x0: float, 
    h: float = 1e-6, 
    h_ord: int = 4, 
    max_iter: int = 2
) -> float:
    """
    Use Newton-Raphson method to find the root of a function f.
    
    Parameters:
    f : Callable[[float], float] - The function for which we want to find the root.
    x0 : float - The initial guess for the root.
    h : float - The step size for calculating the derivative.
    h_ord : int - The order of the Richardson extrapolation to use for derivative approximation.
    max_iter : int - The maximum number of iterations.

    Returns:
    float - The approximate root of the function.
    """

    x = x0
    for _ in range(max_iter):
        # Calculate next approximation
        x_new = x - f(x) / derivative_richardson(f, x, h, h_ord)
        x = x_new

    return x



f = lambda x: x**2 - 2
x0 = 10
exact_root = 1.4142135623730951

# expected root is 2
# iterate from h = 1 to h = 1e-20 and print errors

for h in range(16):
    h = 10**-h
    root = newton_rhapson(f, x0, h=h, h_ord=2, max_iter=5)
    error = abs(root - exact_root)
    print(f"h = {h:.0e}, root = {root:.10f}, error = {error:.10f}")
    


