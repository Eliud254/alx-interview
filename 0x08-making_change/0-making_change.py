#!/usr/bin/python3
"""Making Change Problem 0-making_change.py
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins
    needed to make a given amount of change.

    Args:
        coins (list): List of available coin denominations.
        total (int): The total amount for which change is needed.

    Returns:
        int: Minimum number of coins required to make the change.
        -1: If it is not possible to make the change with the given coins.
    """

    # If the total amount is zero or negative, return -1
    if total <= 0:
        return -1

    # Sort the coins in descending order to
    sorted_coins = sorted(coins, reverse=True)
    count = 0
    remaining_value = total
    index = 0

    # Iterate through the sorted coin list
    while remaining_value > 0 and index < len(sorted_coins):
        # If the current coin can be used to make change
        if remaining_value >= sorted_coins[index]:
            remaining_value -= sorted_coins[index]
            count += 1
        else:
            # Move to the next smaller coin
            index += 1

    # If change cannot be made with the given coins, return -1
    if remaining_value != 0:
        return -1

    return count
