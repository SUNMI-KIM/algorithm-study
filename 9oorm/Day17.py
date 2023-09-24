import sys
from collections import deque

N, M= map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

queue = deque()
visited = [0] * (N + 1)
max_list = []
max_value = 0

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N + 1):
    value = []
    if visited[i]:
        continue
    count = 0
    visited[i] = 1
    queue.append(i)
    
    while queue:
        v = queue.popleft()
        value.append(v)
        for l in graph[v]:
            count += 1
            if visited[l]:
                continue
            queue.append(l)
            visited[l] = 1

    value.sort()
    density = (count // 2) / len(value)

    if max_value < density:
        max_value = density
        max_list = value
    
    elif len(max_list) < len(value):
        max_value = density
        max_list = value
    
    elif max_list[0] > value[0]:
        max_value = density
        max_list = value

for i in max_list:
    print(i, end=" ")