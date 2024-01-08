#!/usr/bin/python3
"""N Queens problem solver."""

import sys

def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(N):
    """Solves the N Queens problem."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_util(N, 0, board, solutions)
    return solutions

def solve_util(N, col, board, solutions):
    """A utility function to solve N Queens problem."""
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_util(N, col + 1, board, solutions) or res
            board[i][col] = 0

    return res

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for solution in solutions:
        print(solution)
