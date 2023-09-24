import sys

N = int(input())

gr, gc = map(int, sys.stdin.readline().split(" "))
pr, pc = map(int, sys.stdin.readline().split(" "))
board = [list(map(str, sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]

dir = {"L" : [0, -1], "D" : [1, 0], "U" : [-1, 0], "R" : [0, 1]}

def count(x, y):
    visited = [[0 for _ in range(N)] for __ in range(N)]
    cnt = 1
    while not visited[x][y]:
        command, repeat = board[x][y][-1], int(board[x][y][0:len(board[x][y]) - 1])
        for _ in range(repeat):
            visited[x][y] = 1
            x = (x + dir[command][0]) % N
            y = (y + dir[command][1]) % N
            if visited[x][y]:
                break
            cnt += 1
    return cnt

goorm = count(gr - 1, gc - 1)
player = count(pr - 1, pc - 1)

if goorm > player:
    print("goorm", goorm)
else:
    print("player", player)