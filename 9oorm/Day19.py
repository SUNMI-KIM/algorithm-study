import sys
from collections import deque

N, M, S, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(prohibition):
    dist = [-1 for _ in range(N + 1)]
    queue = deque()
    visited[S] = 1
    dist[S] = 1
    queue.append(S)
    
    while queue:
        v = queue.popleft()
        for nv in graph[v]:
            if visited[nv] or nv == prohibition:
                continue
            visited[nv] = 1
            queue.append(nv)
            dist[nv] = dist[v] + 1

    return dist[E]

for i in range(1, N + 1):
    if i == S or i == E:
        print(-1)
        continue
    visited = [0 for _ in range(N + 1)]
    result = bfs(i)
    if visited[E]:
        print(result)
    else:
        print(-1)

'''def dfs(route, v, visited, prohibition):

    global result
    global cnt

    if cnt < len(route):
        return
    if v == E:
        result = len(route)
        cnt = result
        return 
    
    for nv in graph[v]:
        if visited[nv] or nv == prohibition:
            continue
        visited[nv] = 1
        route.append(nv)
        dfs(route, nv, visited ,prohibition)
        route.pop()
        visited[nv] = 0


for i in range(1, N + 1):
    if i == S or i == E:
        print(-1)
        continue
    visited[S] = 1
    result = -1
    cnt = float(("inf"))
    dfs([S], S, visited, i)
    print(result)'''