import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for __ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dic = {}
queue = deque()

for i in range(N):
    for r in range(N):
        if visited[i][r] or board[i][r] == 0:
            continue
        if board[i][r] not in dic:
            dic[board[i][r]] = 0
        count = 1
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
                if board[nx][ny] != board[x][y]:
                    continue
                count += 1
                queue.append((nx, ny))
                visited[nx][ny] = 1
        if count >= K:
            dic[board[i][r]] += 1

max_value = 0
max_key = 0
for i in dic.keys():
    if dic[i] > max_value:
        max_key = i
        max_value = dic[i]
    elif dic[i] == max_value:
        max_key = max(i, max_key)
print(max_key)