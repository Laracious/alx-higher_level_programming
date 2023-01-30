#!/usr/bin/python3
import sys

def solve_nqueens(n, row, positions, results):
    if row == n:
        results.append(positions[:])
        return

    for col in range(n):
        positions[row] = col
        safe = True
        for queen in range(row):
            if positions[queen] == col or \
               abs(positions[queen] - col) == abs(queen - row):
                safe = False
                break
        if safe:
            solve_nqueens(n, row + 1, positions, results)

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    results = []
    solve_nqueens(n, 0, [-1] * n, results)
    for result in results:
        print([[i, j] for i, j in enumerate(result)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = int(sys.argv[1])
    nqueens(n)

