#!/usr/bin/python3
"""
N-queen problem solver.
This script solves the N-queen problem for any N > 3 on an NxN chessboard.
"""
import sys


def n_q(t_arr, arr, col, i, n):
    """
    Finds all possible solutions for the N-queen problem and returns them in a list.

    Args:
        t_arr (list): Temporary list to store the current points of a possible solution.
        arr (list): List to store all solutions.
        col (list): List to store columns used by a queen.
        i (int): Current row of the chessboard.
        n (int): Number of queens (or size of the chessboard minus one).

    Returns:
        list: A list of all possible solutions, each solution being a list of queen positions.
    """
    if i > n:
        arr.append(t_arr[:])
        return arr

    for j in range(n + 1):
        if i == 0 or ([i - 1, j - 1] not in t_arr and
                      [i - 1, j + 1] not in t_arr and
                      j not in col):
            if i > 1:
                dia = False
                for k in range(2, i + 1):
                    if ([i - k, j - k] in t_arr) or ([i - k, j + k] in t_arr):
                        dia = True
                        break
                if dia:
                    continue
            t_arr.append([i, j])
            col.append(j)
            n_q(t_arr, arr, col, i + 1, n)
            col.pop()
            t_arr.pop()

    return arr


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_q_arr = n_q([], [], [], 0, n - 1)
    for solution in n_q_arr:
        print(solution:)

