#https://www.acmicpc.net/problem/2606
import sys
from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
queue = deque()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue.appendleft(1)
visited[1] = 1

ans = 0
while queue:
    v = queue.pop()
    for nv in graph[v]:
        if visited[nv]:
            continue
        ans += 1
        visited[nv] = 1
        queue.appendleft(nv)
print(ans)