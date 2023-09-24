import sys
from collections import deque

N, M= map(int, sys.stdin.readline().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
node = [[] for _ in range(N + 1)]

queue = deque()
visited = [0] * (N + 1)
count = 0

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    node[a].append(b)

for i in range(1, N + 1):
    if visited[i]:
        continue
    visited[i] = 1
    queue.append(i)
    count += 1

    while queue:
        v = queue.popleft()
        for l in node[v]:
            if visited[l] or graph[v][l] != graph[l][v]:
                continue
            queue.append(l)
            visited[l] = 1
print(count)