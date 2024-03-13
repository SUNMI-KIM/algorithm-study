#https://www.acmicpc.net/problem/12865
import sys

N, K = map(int, sys.stdin.readline().split())
W = [0] * (N + 1)
V = [0] * (N + 1)
dp = [[0 for _ in range(K + 1)] for __ in range(N + 1)]

for i in range(1, N + 1):
    W[i], V[i] = map(int, sys.stdin.readline().split())

for i in range(1, N + 1):
    for r in range(K + 1):
        if r < W[i]:
            dp[i][r] = dp[i - 1][r]
        else:
            dp[i][r] = max(dp[i - 1][r], dp[i - 1][r - W[i]] + V[i])

print(dp[N][K])