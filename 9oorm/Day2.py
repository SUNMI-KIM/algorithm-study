# 처음에 최적화 안한 코드 O(n^2)
N = int(input())
T, M = map(int, input().split())

for i in range(N):
    c = int(input())
    while (c > 60):
        c -= 60
        T += 1
    M += c
    if M >= 60:
        T += 1
        M -= 60

    T = T % 24
print(T, M)

# 최적화 한 코드 O(n)
N = int(input())
T, M = map(int, input().split())

for i in range(N):
    c = int(input())
    T += c // 60
    M += c % 60
    if M >= 60:
        M -= 60
        T += 1
    T = T % 24

print(T, M)