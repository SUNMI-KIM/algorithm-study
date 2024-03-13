from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
c = []
h = []

for i in range(N):
    for r in range(N):
        if board[i][r] == 1:
            h.append([i, r])
        elif board[i][r] == 2:
            c.append([i, r])

clist = list(combinations(c, 3))
