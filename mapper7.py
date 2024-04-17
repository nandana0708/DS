# mapper.py

import random

def generate_random_numbers(n):
    numbers = [random.randint(1, 100) for _ in range(n)]  # Generate n random natural numbers
    return numbers

def mapper(number):
    if number % 2 == 0:
        return ("even", 1)
    else:
        return ("odd", 1)

if __name__ == "__main__":
    n = 10  # Number of random natural numbers to generate
    numbers = generate_random_numbers(n)
    for number in numbers:
        result = mapper(number)
        if result:
            print(f"{result[0]}\t{result[1]}")

