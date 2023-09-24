import sys

N, K = map(int, sys.stdin.readline().split())
ground = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
board = [[0 for _ in range(N)] for __ in range(N)]

dx = [1, 0, -1, 0, 0]
dy = [0, 1, 0, -1, 0]

max_value = 0
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    for dir in range(5):
        nx = x + dx[dir] - 1
        ny = y + dy[dir] - 1
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if ground[nx][ny] == "#":
            continue
        if ground[nx][ny] == "0":
            board[nx][ny] += 1
        if ground[nx][ny] == "@":
            board[nx][ny] += 2
        max_value = max(max_value, board[nx][ny])

print(max_value)