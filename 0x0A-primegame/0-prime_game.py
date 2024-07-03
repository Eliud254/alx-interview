#!/usr/bin/python3
"""Prime game"""


def generate_prime_numbers(limit):
    """
    Generate a list of prime numbers up to a specified limit.

    Args:
        limit (int): The upper boundary for generating prime numbers.

    Returns:
        list: A list containing all prime numbers up to the specified limit.
    """
    primes = []  # List to store prime numbers
    sieve_list = [True] * (limit + 1)  # Boolean list to mark non-prime numbers

    for potential_prime in range(2, limit + 1):
        if sieve_list[potential_prime]:  # Check if the number is prime
            primes.append(potential_prime)  # Add prime number to the list
            for multiple in range(potential_prime, limit + 1, potential_prime):
                sieve_list[multiple] = False  # Mark multiples as non-prime

    return primes  # Return the list of prime numbers


def is_winner(num_rounds, round_values):
    """
    Determine the winner of the prime number game.

    Args:
        num_rounds (int): The number of rounds in the game.
        round_values (list): A list specifying the upper limit
        for prime numbers
                             to generate in each round.

    Returns:
        str: The name of the winner ("Maria" or "Ben")
        or None if there is no winner.
    """
    if not num_rounds or not round_values:  # Validate input
        return None

    maria_score = ben_score = 0  # Initialize scores

    for i in range(num_rounds):
        primes = generate_prime_numbers(round_values[i])

        if len(primes) % 2 == 0:
            ben_score += 1  # Even number of primes increments Ben's score
        else:
            maria_score += 1  # Odd number of primes increments Maria's score

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"

    return None
