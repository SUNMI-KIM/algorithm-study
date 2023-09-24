import sys
from collections import deque

N, K, Q = map(int, sys.stdin.readline().split())
board = [list(str(sys.stdin.readline().strip())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, alphabet):
    delete_list = []
    visited = [[0 for _ in range(N)] for __ in range(N)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        delete_list.append((x, y))
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or alphabet != board[nx][ny]:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = 1

    if len(delete_list) >= K:
        delete(delete_list)

def delete(delete_list):
    for x, y in delete_list:
        board[x][y] = "."

for _ in range(Q):
    x, y, d = map(str, sys.stdin.readline().split())
    x, y = int(x) - 1, int(y) - 1
    board[x][y] = d
    bfs(x, y, d)

for arr in board:
    print("".join(arr))