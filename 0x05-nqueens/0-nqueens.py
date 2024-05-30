#!/usr/bin/python3
"""
The Solution to the N-queens problem.
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Recursively solves the N-queens problem by placing queens one row at a time.

    Args:
        r (int): The current row being explored.
        n (int): The size of the board (n x n) and the number of queens.
        cols (set): Columns where queens are already placed.
        pos (set): Positive diagonals where queens are already placed.
        neg (set): Negative diagonals where queens are already placed.
        board (list): The current state of the board, represented as a list of lists.
    """
    if r == n:
        # All queens are placed successfully, store the solution
        res = []
        for j in range(len(board)):
            for k in range(len(board[j])):
                if board[j][k] == 1:
                    res.append([j, k])
        print(res)
        return

    for c in range(n):
        # Check if the position is safe for the queen
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        # Place the queen and mark the positions
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        # Recurse to place the next queen
        backtrack(r + 1, n, cols, pos, neg, board)

        # Remove the queen and backtrack
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solves the N-queens problem and prints all solutions.

    Args:
        n (int): The number of queens (and the size of the chessboard).
    """
    # Initialize sets to track columns and diagonals used by queens
    cols = set()
    pos_diag = set()
    neg_diag = set()
    
    # Initialize the board with zeros
    board = [[0] * n for _ in range(n)]

    # Start the backtracking algorithm from the first row
    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

