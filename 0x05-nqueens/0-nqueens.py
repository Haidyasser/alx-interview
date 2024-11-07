#!/usr/bin/python3
"""N queens
"""
import sys


def isSafe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[i] == row or board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solveNQUtil(board, col):
    """Use backtracking to solve N Queen problem"""
    n = len(board)
    if col == n:
        print(str([[i, board[i]] for i in range(n)]))
        return
    for i in range(n):
        if isSafe(board, i, col):
            board[col] = i
            solveNQUtil(board, col + 1)
            board[col] = -1


def solveNQ(arg):
    """
    Solve N
    """
    if len(arg) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(arg[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1 for i in range(n)]
    solveNQUtil(board, 0)


if __name__ == "__main__":
    solveNQ(sys.argv)
