#!/usr/bin/python3
"""
Prime Game module
"""


def isWinner(x, nums):
    """
    Determine the winner of each game
    """
    if not nums or x < 1:
        return None

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def calculate_primes(n):
        primes = [0] * (n + 1)
        primes[0] = primes[1] = 0
        for i in range(2, n + 1):
            if is_prime(i):
                primes[i] = 1
        return primes

    def calculate_cumulative_primes(primes):
        cumulative = [0] * len(primes)
        count = 0
        for i in range(len(primes)):
            if primes[i] == 1:
                count += 1
            cumulative[i] = count
        return cumulative

    def find_winner(primes, cumulative):
        if cumulative[-1] % 2 == 0:
            return "Ben"
        return "Maria"

    winners = []
    for n in nums:
        primes = calculate_primes(n)
        cumulative_primes = calculate_cumulative_primes(primes)
        winners.append(find_winner(primes, cumulative_primes))

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
