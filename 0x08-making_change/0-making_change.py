#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin values.
        total (int): The amount total to meet.

    Returns:
        int: Fewest number of coins needed to meet total.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
