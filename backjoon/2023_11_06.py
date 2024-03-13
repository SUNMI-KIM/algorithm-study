#https://www.acmicpc.net/problem/11559

import sys
from collections import deque

board = [list(str(sys.stdin.readline().strip())) for _ in range(12)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

'''def print_arr():
    print("-------")
    for i in range(12):
        for r in range(6):
            print(board[i][r], end="")
        print()'''

def delete(puyo):
    for x, y in puyo:
        board[x][y] = "."

def bfs(x, y, color):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    puyo = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if visited[nx][ny]:
                continue
            if color != board[nx][ny]:
                continue
            puyo.append((nx, ny))
            queue.append((nx, ny))
            visited[nx][ny] = 1
    
    if len(puyo) >= 4:
        delete(puyo)
        return True
    return False

def down():
    for i in range(6):
        index = 11
        for r in range(11, -1, -1):
            if board[index][i] != ".":
                index -= 1
                continue
            if board[r][i] == ".":
                continue
            board[index][i] = board[r][i]
            board[r][i] = '.'
            index -= 1

count = 0
flag = True
while flag:
    flag = False
    visited = [[0 for _ in range(6)] for __ in range(12)]
    for i in range(11, -1, -1):
        for r in range(6):
            if board[i][r] == ".":
                continue
            if bfs(i, r, board[i][r]):
                flag = True
    down()
    #print_arr()
    count += 1

print(count - 1)