#https://www.acmicpc.net/problem/15663

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0] * 10
isused = [0] * 10
sequence = sorted(list(map(int, sys.stdin.readline().split())))

def solve(k):
    if M == k:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        return 
    tmp = 0
    for i in range(N):
        if (not isused[i] and tmp != sequence[i]):
            arr[k] = sequence[i]
            isused[i] = 1
            tmp = arr[k]
            solve(k + 1)
            isused[i] = 0
            
solve(0)

#https://www.acmicpc.net/problem/15664

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0] * 10
isused = [0] * 10
sequence = sorted(list(map(int, sys.stdin.readline().split())))

def solve(k, l):
    if M == k:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        return 
    tmp = 0
    for i in range(l, N):
        if (not isused[i] and tmp != sequence[i]):
            arr[k] = sequence[i]
            isused[i] = 1
            tmp = arr[k]
            solve(k + 1, i)
            isused[i] = 0
            
solve(0, 0)

#https://www.acmicpc.net/problem/15665

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0] * 10
isused = [0] * 10
sequence = sorted(list(map(int, sys.stdin.readline().split())))

def solve(k):
    if M == k:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        return 
    tmp = 0
    for i in range(N):
        if (tmp != sequence[i]):
            arr[k] = sequence[i]
            tmp = arr[k]
            solve(k + 1)
            
solve(0)

#https://www.acmicpc.net/problem/15666

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0] * 10
isused = [0] * 10
sequence = sorted(list(map(int, sys.stdin.readline().split())))

def solve(k, l):
    if M == k:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        return 
    tmp = 0
    for i in range(l, N):
        if (tmp != sequence[i]):
            arr[k] = sequence[i]
            tmp = arr[k]
            solve(k + 1, i)
            
solve(0, 0)

#https://www.acmicpc.net/problem/9663

N = int(input())
cnt = 0
isused1 = [False] * N
isused2 = [False] * (N * 2)
isused3 = [False] * (N * 2)

def solve(cur):
    if cur == N:
        global cnt
        cnt += 1
        return
    for i in range(N):
        if isused1[i] or isused2[cur + i] or isused3[cur - i + N - 1]:
            continue
        isused1[i] = True
        isused2[cur + i] = True
        isused3[cur - i + N - 1] = True
        solve(cur + 1)
        isused1[i] = False
        isused2[cur + i] = False
        isused3[cur - i + N - 1] = False

solve(0)
print(cnt)

# https://www.acmicpc.net/problem/9663

N = int(input())
board = [0] * 20
cnt = 0


def check(row):
    for prev_row in range(row):
        if board[prev_row] == board[row] or row - prev_row == abs(board[row] - board[prev_row]):
            return False
    return True


def solve(row):
    if row == N:
        global cnt
        cnt += 1
        return
    for col in range(N):
        board[row] = col
        if check(row):
            solve(row + 1)


solve(0)
print(cnt)