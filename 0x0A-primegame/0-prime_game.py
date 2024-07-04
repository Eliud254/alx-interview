#!/usr/bin/python3
""" Prime Game """


def generatePrimeNumbers(limit):
    """
    Generate a list of prime numbers up to a given limit.

    Args:
        limit (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers up to the given limit.
    """
    # List to store prime numbers
    primes = []
    # Boolean list to mark prime status of numbers from 0 to limit
    sieveList = [True] * (limit + 1)

    # Iterate over numbers from 2 to limit
    for potentialPrime in range(2, limit + 1):
        # If the number is prime, according to the sieve
        if sieveList[potentialPrime]:
            # Add it to the list of primes
            primes.append(potentialPrime)
            # Mark multiples of the number as non-prime
            for multiple in range(potentialPrime, limit + 1, potentialPrime):
                sieveList[multiple] = False

    return primes


def isWinner(numRounds, roundValues):
    """
    Determine the winner of the Prime Game.

    Args:
        numRounds (int): The number of rounds in the game.
        roundValues (list): The upper limits for generating
        prime numbers in each round.

    Returns:
        str: The name of the winner ('Maria' or 'Ben'
        ) or None if there's no winner.
    """
    # Check for valid input
    if not numRounds or not roundValues:
        return None

    # Initialize scores for Maria and Ben
    maria_score = ben_score = 0

    # Play each round
    for i in range(numRounds):
        # Generate prime numbers up to the current round's limit
        primes = generatePrimeNumbers(roundValues[i])

        # Check the count of prime numbers
        if len(primes) % 2 == 0:
            # Even count: Ben wins this round
            ben_score += 1
        else:
            # Odd count: Maria wins this round
            maria_score += 1

    # Determine the overall winner
    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"

    return None
