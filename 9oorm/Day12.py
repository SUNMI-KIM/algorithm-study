import sys
from collections import deque

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for __ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0
queue = deque()

for i in range(N):
    for r in range(N):
        if visited[i][r] or board[i][r] == 0:
            continue
        count += 1
        queue.append((i, r))
        visited[i][r] = 1
        while queue:
            x, y = queue.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if visited[nx][ny] or board[nx][ny] == 0:
                    continue
                queue.append((nx, ny))
                visited[nx][ny] = 1

print(count)

