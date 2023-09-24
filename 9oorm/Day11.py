N = int(input())
A, B = map(int, input().split())

dp = [10000000] * (N + 1)
dp[0] = 0

for i in [A, B]:
    for r in range(i, N + 1):
        dp[r] = min(dp[r], dp[r - i] + 1)

if dp[-1] >= 10000000:
    print(-1)
else:
    print(dp[-1])
        