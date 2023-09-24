import sys

N = int(input())
max_value = 0
board1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def rotate():
    tmp = []
    for x in range(N):
        tmp.append([])
        for y in range(N):
            tmp[x].append(board2[x][y])
    for i in range(N):
        for r in range(N):
            board2[r][N - i - 1] = tmp[i][r]

def tilt(dir):
    while dir > 0:
        dir -= 1
        rotate()
    
    for i in range(N):
        tilted = [0] * N
        idx = 0
        for r in range(N):
            if board2[i][r] == 0:
                continue
            if tilted[idx] == 0:
                tilted[idx] = board2[i][r]
            elif tilted[idx] == board2[i][r]:
                tilted[idx] *= 2
                idx += 1
            else:
                idx += 1
                tilted[idx] = board2[i][r]
        for r in range(N):
            board2[i][r] = tilted[r]

def check():
    global max_value
    for x in range(N):
        for y in range(N):
            max_value = max(board2[x][y], max_value) 

for tmp in range(1024):
    board2 = []
    for x in range(N):
        board2.append([])
        for y in range(N):
            board2[x].append(board1[x][y])
    brute = tmp
    for r in range(5):
        dir = brute % 4
        brute //= 4
        tilt(dir)
    check()
print(max_value)
    



