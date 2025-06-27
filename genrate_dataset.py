import numpy as np
import csv
from sympy import sieve


def generate_primes(n: int):

    primes = np.array([i for i in sieve.primerange(n)])
    is_prime_vec = np.zeros(n + 1, dtype=np.bool_)
    is_prime_vec[primes] = True

    return primes, is_prime_vec


def compute_g(is_prime_vec: np.ndarray, primes: np.ndarray, E: int) -> int:

    assert E < len(is_prime_vec)
    assert E % 2 == 0
    E_half = int(0.5 * E)

    # initialization
    count = 0  # number of prime pairs

    # we loop over all the prime numbers smaller than or equal to half of E
    i_max = np.searchsorted(primes, E_half, side="right")
    for i in range(i_max):
        if is_prime_vec[E - primes[i]]:
            count += 1

    return count






        
with open('data.csv', 'a') as csvfile:
        fieldnames = ['Even_number', 'combination']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(4,10000000):
            if not i %2:
                primes, is_prime_vec = generate_primes(i)
                g = compute_g(is_prime_vec, primes, i)
                writer.writerow({'Even_number': f'{i}', 'combination': f'{g}'})