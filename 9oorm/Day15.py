import sys

N, K = map(int, sys.stdin.readline().split())
fruit = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
piece = []

for i in range(len(fruit)):
    P, C = fruit[i][0], fruit[i][1]
    piece.append([C // P, i])

fullness = 0
piece.sort(reverse=True)
for full, index in piece:
    if K >= fruit[index][0]:
        K -= fruit[index][0]
        fullness += fruit[index][1]
    else:
        fullness += full * K
        break

print(fullness)
    

