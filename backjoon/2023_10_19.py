#https://www.acmicpc.net/problem/11724
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
ans = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for v in range(1, N + 1):
    if visited[v]:
        continue
    ans += 1
    queue = deque()
    visited[v] = 1
    queue.append(v)

    while queue:
        vertex = queue.popleft()
        for nv in graph[vertex]:
            if visited[nv]:
                continue
            visited[nv] = 1
            queue.append(nv)
print(ans)