# Function to return the nearest prime number less than or equal to n
from math import floor, sqrt

def prime(n):
    if n == 2: 
        return 0  # The nearest prime to 2 is 2 itself

    # Adjust n to make it odd if it’s even, as even numbers > 2 are not prime
    if n % 2 == 0:
        n -= 1
    else:
        n -= 2

    # Check each odd number from n downwards for primality
    for i in range(n, 2, -2):
        is_prime = True

        # Check if the current number i is prime
        for j in range(3, floor(sqrt(i)) + 1, 2):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            return i

    # If no primes are found, return 2 (covers cases where n < 3)
    return 2

# Driver Code
n = 9
print(prime(n))
