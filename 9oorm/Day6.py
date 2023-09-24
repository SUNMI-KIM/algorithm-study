N = int(input())
S = input()
substr = set()
substrs = []

for i in range(1, N - 1):
    for r in range(i + 1, N):
        substr.add(S[:i])
        substr.add(S[i : r])
        substr.add(S[r:])
        substrs.append([S[:i], S[i : r], S[r:]])

max_cnt = 0
substr = sorted(list(substr))
for i in range(len(substrs)):
    count = 0
    for r in range(3):
        count += substr.index(substrs[i][r])
    max_cnt = max(count, max_cnt)

print(max_cnt + 3) #인덱스 값이기 때문에 3을 더해준다.


'''N = int(input())
S = input()
substr = set()
substrs = []

for i in range(1, N - 1):
    for r in range(i + 1, N):
        substr.add(S[:i])
        substr.add(S[i : r])
        substr.add(S[r:])
        substrs.append([S[:i], S[i : r], S[r:]])

max_cnt = 0
substr = sorted(list(substr))
print(substr)
for i in range(len(substrs)):
    print(substrs[i])
    count = 0
    for r in range(3):
        count += substr.index(substrs[i][r])
    max_cnt = max(count, max_cnt)
    print(count)

print(len(substr) * 2 + N - 4 if N > 3 else 6)'''