#!/usr/bin/python3
"""Prime Game"""


def isPrime(n):
    """check if a number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Prime Game"""
    if x < 1 or nums is None:
        return None

    maria = 0
    ben = 0
    for n in nums:
        mariaWin = False
        for i in range(1, n+1):
            if isPrime(i):
                mariaWin = not mariaWin
        if mariaWin:
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return "Maria"
    if maria < ben:
        return "Ben"
    return None
