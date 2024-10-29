import argparse
import math
from finite_differences import newton_rhapson

def select_function(fun_id):
    if fun_id == 1:
        return lambda x: x**2 - 2, 1.4142135623730951  # Exact root for f(x) = x^2 - 2
    elif fun_id == 2:
        return lambda x: math.cos(x) - x, 0.7390851332151607  # Exact root for f(x) = cos(x) - x
    else:
        raise ValueError("Unknown function ID. Use 1 for x^2 - 2 or 2 for cos(x) - x.")

def main():
    parser = argparse.ArgumentParser(description="Newton-Raphson iteration with error analysis.")
    parser.add_argument("fun", type=int, help="Function ID (1 for x^2 - 2, 2 for cos(x) - x)")
    parser.add_argument("x0", type=float, help="Initial guess for root")
    parser.add_argument("--h_ord", type=int, choices=[2, 4], default=2, help="Richardson extrapolation order (2 or 4)")
    parser.add_argument("--max_iter", type=int, default=2, help="Maximum number of iterations")
    args = parser.parse_args()

    # Select function and exact root based on the provided function ID
    f, exact_root = select_function(args.fun)
    
    print("Newton-Raphson Iteration Error Analysis:")
    print(f"Function ID = {args.fun}, Initial x0 = {args.x0}, h_ord = {args.h_ord}, max_iter = {args.max_iter}")
    print("-" * 50)
    print("h           | root            | error")
    print("-" * 50)

    # Iterate from h = 10^0 to h = 10^-16
    for h_exp in range(16):
        h = 10**-h_exp
        root = newton_rhapson(f, args.x0, h=h, h_ord=args.h_ord, max_iter=args.max_iter)
        error = abs(root - exact_root)
        print(f"h = {h:.0e}, root = {root:.10f}, error = {error:.10f}")

if __name__ == "__main__":
    main()
