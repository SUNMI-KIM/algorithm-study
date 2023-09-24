import sys

N, M = map(int, sys.stdin.readline().split())
board = [[{"horizon" : 0, "vertical" : 0} for _ in range(N)] for __ in range(N)] #vertical 수직선 | , horizon 수평선 ㅡ 
dir = {"R" : [0, 1], "D" : [1, 0], "L" : [0, -1], "U" : [-1, 0]}

def draw(direction, line, x, y):
    while (0 <= x < N and 0 <= y < N):
        board[x][y][line] += 1
        x += dir[direction][0]
        y += dir[direction][1]

for _ in range(M):
    x, y, direction = map(str, sys.stdin.readline().split())
    if direction == "U" or direction == "D":
        draw(direction, "vertical", int(x) - 1, int(y) - 1)
    else:
        draw(direction, "horizon", int(x) - 1, int(y) - 1)

answer = 0
for i in range(N):
    for r in range(N):
        answer += board[i][r]["horizon"] * board[i][r]["vertical"]
print(answer)