import numpy as np
import matplotlib.pyplot as plt

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

import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

def plot_newton_rhapson(
    f: Callable[[float], float], 
    f_prime: Callable[[float], float], 
    x0: float, 
    h: float = 1e-6, 
    h_ord: int = 4, 
    max_iter: int = 2
) -> float:
    x_values = [x0]
    f_values = [f(x0)]
    f_prime_values = []
    f_prime_actual_values = []
    
    for _ in range(max_iter):
        f_derivative = derivative_richardson(f, x0, h, h_ord)
        f_prime_values.append(f_derivative)
        f_prime_actual_values.append(f_prime(x0))

        x0 = x0 - f_values[-1] / f_derivative
        
        x_values.append(x0)
        f_values.append(f(x0))
    
    # Generate values for plotting the actual function f(x)
    x_margin = 0.2 * (max(x_values) - min(x_values))
    x_plot = np.linspace(min(x_values) - x_margin, max(x_values) + x_margin, 1000)
    f_plot = f(x_plot)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, f_plot, label='f(x)', color='blue')
    
    # Define y-axis margin and set limits
    y_margin = 0.1 * (max(f_values) - min(f_values))
    plt.ylim(min(f_values) - y_margin, max(f_values) + y_margin)
    
    # Plot the initial guess as a green dot
    plt.scatter(x_values[0], f_values[0], color='green', label='Initial Guess')
    
    # Plot the Newton-Raphson points as red dots
    plt.scatter(x_values[1:], f_values[1:], color='red', label='Newton-Raphson Points')
    
    # Plot tangent lines at each Newton-Raphson point
    for i, (x, y, fp) in enumerate(zip(x_values, f_values, f_prime_values)):
        # Create tangent line points
        tangent_x = np.linspace(x - x_margin, x + x_margin, 100)
        tangent_y = y + fp * (tangent_x - x)
        plt.plot(tangent_x, tangent_y, 'orange', linestyle='--', linewidth=0.8, label='Tangent at Iteration' if i == 0 else "")

    
    # Plot the actual tangent lines at each Newton-Raphson point

    # Customize plot
    plt.title('Newton-Raphson Iteration with Tangent Lines')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.legend()
    plt.grid()
    plt.show()
    
    return x_values[-1]  # Return the last x value after iterations


    
f = lambda x: x**2 - 2
f_prime = lambda x: 2*x
x0 = -10

plot_newton_rhapson(f, f_prime, x0, h=1e-6, h_ord=4, max_iter=2)


