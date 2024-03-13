#https://www.acmicpc.net/problem/2580

import sys

def print_board():
    for x in range(9):
        for y in range(9):
            print(board[x][y], end = " ")
        print()

def check_move(x, y, num):
    for i in range(9):
        if board[x][i] == num:
            return False
        if board[i][y] == num:
            return False
    return True

def check_Three(x, y, num):
    for nx in range(x // 3 * 3, x // 3 * 3 + 3):
        for ny in range(y // 3 * 3, y // 3 * 3 + 3):
            if board[nx][ny] == num:
                return False
    return True

def dfs(cur):
    if cur == len(blank):
        print_board()
        exit()

    x, y = blank[cur][0], blank[cur][1]
    for i in range(1, 10):
        if check_move(x, y, i) and check_Three(x, y, i):
            board[x][y] = i
            dfs(cur + 1)
            board[x][y] = 0

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = []
for x in range(9):
    for y in range(9):
        if board[x][y] == 0:
            blank.append([x, y])
dfs(0)
print_board()