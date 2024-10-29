
import argparse

from fp_arithmetics_and_errors import harmonic_sum

def main():
    parser = argparse.ArgumentParser(description="Calculate the harmonic sum of a number.")
    
    # Define the command 'hsum' and an integer argument 'n'
    parser.add_argument("command", choices=["hsum"], help="Command to execute")
    parser.add_argument("n", type=int, help="The integer for the harmonic sum calculation")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call harmonic_sum if command is 'hsum'
    if args.command == "hsum":
        result = harmonic_sum(args.n)
        print(f"Harmonic sum of {args.n} is {result}")

if __name__ == "__main__":
    main()
