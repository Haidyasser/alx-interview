#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes"""
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """Prime Game"""

    if x < 1 or not nums:
        return None
    n = max(nums)
    primes = seive(n)

    maria = ben = 0
    for i in nums:
        primes_count = sum(primes[:i+1])
        if primes_count % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria == ben:
        return None
    return "Maria" if maria > ben else "Ben"
