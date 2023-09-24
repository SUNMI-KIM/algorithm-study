import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N + 1):
    graph[i].sort()

def dfs(visited, v, count):
    visited[v] = 1
    
    for i in graph[v]:
        if visited[i]:
            continue
        dfs(visited, i, count + 1)
    
    print(count, v)
    exit()
    
dfs([0] * (N + 1), V, 1)