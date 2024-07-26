#!/usr/bin/python3
""" Prime Game """


def generatePrimeNumbers(limit):
    """
    Generate a list of primes up to limit.

    Args:
        limit (int): Upper limit for generating primes.

    Returns:
        list: List of prime numbers up to limit.
    """
    primes = []
    sieveList = [True] * (limit + 1)

    for potentialPrime in range(2, limit + 1):
        if sieveList[potentialPrime]:
            primes.append(potentialPrime)
            for multiple in range(potentialPrime, limit + 1, potentialPrime):
                sieveList[multiple] = False

    return primes


def isWinner(numRounds, roundValues):
    """
    Determine the game winner.

    Args:
        numRounds (int): Number of game rounds.
        roundValues (list): List of round values.

    Returns:
        str: Winner's name or None.
    """
    if not numRounds or not roundValues:
        return None

    maria_score = 0
    ben_score = 0

    for i in range(numRounds):
        primes = generatePrimeNumbers(roundValues[i])

        if len(primes) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None
