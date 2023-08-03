#https://www.acmicpc.net/problem/15649

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] * 10
isused = [0] * 10

def solve(k):
    if M == k:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        return 
    for i in range(1, N + 1):
        if (not isused[i]):
            arr[k] = i
            isused[i] = 1
            solve(k + 1)
            isused[i] = 0
    
solve(0)

#https://www.acmicpc.net/problem/15650

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] * 10
isused = [0] * 10

def solve(k, l):
    if M == k:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        return 
    
    for i in range(l, N + 1):
        if (not isused[i]):
            arr[k] = i
            isused[i] = 1
            solve(k + 1, i)
            isused[i] = 0

solve(0, 1)

#https://www.acmicpc.net/problem/15651

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] * 10

def solve(k):
    if M == k:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        return 
    
    for i in range(1, N + 1):
        arr[k] = i
        solve(k + 1)

solve(0)

#https://www.acmicpc.net/problem/15652

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] * 10

def solve(k, l):
    if M == k:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        return 
    
    for i in range(l, N + 1):
        arr[k] = i
        solve(k + 1, i)

solve(0, 1)

#https://www.acmicpc.net/problem/15654

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
    for i in range(N):
        if (not isused[i]):
            arr[k] = sequence[i]
            isused[i] = 1
            solve(k + 1)
            isused[i] = 0
    
solve(0)

#https://www.acmicpc.net/problem/15655

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
    for i in range(l, N):
        if (not isused[i]):
            arr[k] = sequence[i]
            isused[i] = 1
            solve(k + 1, i)
            isused[i] = 0
    
solve(0, 0)

#https://www.acmicpc.net/problem/15656

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0] * 10
sequence = sorted(list(map(int, sys.stdin.readline().split())))

def solve(k):
    if M == k:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        return 
    for i in range(N):
        arr[k] = sequence[i]
        solve(k + 1)
    
solve(0)

#https://www.acmicpc.net/problem/15657

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0] * 10
sequence = sorted(list(map(int, sys.stdin.readline().split())))

def solve(k, l):
    if M == k:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        return 
    for i in range(l, N):
        arr[k] = sequence[i]
        solve(k + 1, i)
    
solve(0, 0)