import sys
from typing import List
from random import seed, shuffle

def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def primes(count: int) -> List[int]:
    prime_numbers = []
    num = 2
    while len(prime_numbers) < count:
        if is_prime(num):
            prime_numbers.append(num)
        num += 1
    return prime_numbers

def checksum(x: List[int]) -> int:
    result = 0
    for num in x:
        result = (result + num) * 113 % 10_000_007
    return result

def pipeline(seed_value: int) -> int:
    seed(seed_value)
    prime_numbers = primes(1000)
    shuffle(prime_numbers)
    return checksum(prime_numbers)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 task.py seed_value")
        sys.exit(1)
    
    seed_value = int(sys.argv[1])
    print(pipeline(seed_value))