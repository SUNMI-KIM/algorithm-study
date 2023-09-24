def bfs(x, y):
    for dir in range(8):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if M[nx][ny] == "M":
            continue
        M[nx][ny] += 1

def count():
    count = 0
    for x in range(N):
        for y in range(N):
            if M[x][y] == K:
                count += 1
    return count
 
N, K = map(int, input().split())

M = [[0 if __ == "0" else "M" for __ in input().split()] for _ in range(N)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

for i in range(N):
    for r in range(N):
        if M[i][r] == "M":
            bfs(i, r)

print(count())