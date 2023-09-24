N = int(input())
count = 0

if N >= 14:
    count += N // 14
    N %= 14
if N >= 7:
    count += N // 7
    N %= 7
count += N

print(count)

