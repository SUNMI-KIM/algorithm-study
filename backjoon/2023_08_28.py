#https://www.acmicpc.net/problem/1260
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N + 1):
    graph[i].sort()

def bfs(visited):
    queue = deque()
    visited[V] = 1
    queue.append(V)

    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if visited[i]:
                continue
            visited[i] = 1
            queue.append(i)

def dfs(visited, v):
    visited[v] = 1
    print(v, end = " ")
    
    for i in graph[v]:
        if visited[i]:
            continue
        dfs(visited, i)
    
dfs([0] * (N + 1), V)
print()
bfs([0] * (N + 1))