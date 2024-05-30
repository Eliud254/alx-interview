#!/usr/bin/python3
"""
The Solution to the N-queens problem.
"""

import sys


def solve_nqueens(n):
    """
    To Solves the N-queens problem and prints all solutions.

    Args:
        n (int): The number of queens (and the size of the chessboard).
    """
    def backtrack(row, n, cols, pos_diag, neg_diag, board):
        """
        Recursively solves the N-queens problem by placing queens one row at a time.

        Args:
            row (int): The current row being explored.
            n (int): The size of the board (n x n) and the number of queens.
            cols (set): Columns where queens are already placed.
            pos_diag (set): Positive diagonals where queens are already placed.
            neg_diag (set): Negative diagonals where queens are already placed.
            board (list): The current state of the board, represented as a list of lists.
        """
        if row == n:
            res = []
            for r in range(n):
                for c in range(n):
                    if board[r][c] == 1:
                        res.append([r, c])
            print(res)
            return

        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            board[row][col] = 1

            backtrack(row + 1, n, cols, pos_diag, neg_diag, board)

            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            board[row][col] = 0

    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


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
    
    solve_nqueens(n)
