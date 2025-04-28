import sys
import math
import multiprocessing
import time

# Increase the maximum numbers of digits for integer conversion
sys.set_int_max_str_digits(100000)

# Function to compute factorial of a given number
def fact(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    num = [5000, 6000, 7000, 8000]
    start_time = time.time()

    # Create a pool of worker processors
    with multiprocessing.Pool() as pool:
        result = pool.map(fact, num)

    end_time = time.time()

    print(f"Results: {result}")
    print(f"The time taken is {end_time - start_time} seconds")
