#!/usr/bin/python3
"""
N Queens puzzle solver using backtracking.
"""
import sys


def print_usage_and_exit():
    """Prints the usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_input():
    """Validates the command-line arguments."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(board, row, col):
    """Checks if a queen can be placed at board[row][col]."""
    for i in range(row):if board[i] == col or            board[i] - i == col - row or            board[i] + i == col + row:
            return False
    return True


def solve_nqueens(row, n, board):
    """Recursively solves the N Queens puzzle using backtracking."""
    if row == n:solution = [[i, board[i]] for i in range(n)]
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(row + 1, n, board)def main():
    """Main execution entry point."""
    n = validate_input()board = [0] * n
    solve_nqueens(0, n, board)


if __name__ == "__main__":
    main()
