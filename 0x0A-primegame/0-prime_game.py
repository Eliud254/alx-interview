#!/usr/bin/python3
"""Prime game"""

def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to a specified
    limit using the Sieve of Eratosthenes.

    Args:
        n (int): The upper boundary for generating prime numbers.

    Returns:
        list: A list containing boolean values indicating
        prime status for each number up to n.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, n + 1, start):
                sieve[multiple] = False
    return sieve


def count_primes_up_to(n, sieve):
    """
    Count the number of prime numbers up to a specified limit.

    Args:
        n (int): The upper boundary for counting prime numbers.
        sieve (list): The sieve list indicating prime status for each number.

    Returns:
        int: The count of prime numbers up to the specified limit.
    """
    return sum(sieve[:n + 1])


def is_winner(x, nums):
    """
    Determine the winner of the prime number game.

    Args:
        x (int): The number of rounds in the game.
        nums (list): A list specifying the upper limit
        for prime numbers to generate in each round.

    Returns:
        str: The name of the player that won the most rounds
        ("Maria" or "Ben") or None if the winner cannot be determined.
    """
    if not x or not nums:
        return None

    max_num = max(nums)
    sieve = sieve_of_eratosthenes(max_num)

    maria_score = ben_score = 0

    for n in nums:
        prime_count = count_primes_up_to(n, sieve)
        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None


# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(is_winner(5, [2, 5, 1, 4, 3])))
