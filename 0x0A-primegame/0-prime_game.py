#!/usr/bin/python3
"""Prime Game"""


def seive(n):
    """Sieve of Eratosthenes"""
    prime = [True for i in range(n+1)]
    for i in range(2, n+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return prime


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