#https://www.acmicpc.net/problem/1085
a, b, c, d = map(int, input().split())
li = []
li.append(c - a)
li.append(d - b)
li.append(a)
li.append(b)
print(min(li))

#https://www.acmicpc.net/problem/1100
import sys
li = []
result = 0
for i in range(0, 8):
    li.append(sys.stdin.readline())
for i in range(0, 8):
    for r in range(0, 8):
        if i % 2 != 0 and r % 2 != 0 and li[i][r] == "F":
            result += 1
        if i % 2 == 0 and r % 2 == 0 and li[i][r] == "F":
            result += 1
print(result)

#https://www.acmicpc.net/problem/1157
a = input()
a = a.upper()
dic = {}
for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
result = [k for k,v in dic.items() if max(dic.values()) == v]
if len(result) == 1:
    print(result[0])
else:
    print("?")

#https://www.acmicpc.net/problem/1159
a = int(input())
dic = {}
result = []
for i in range(0, a):
    b = input()
    if b[0] not in dic:
        dic[b[0]] = 1
    else: 
        dic[b[0]] += 1
for i in dic.keys():
    if dic[i] > 4:
        result.append(i)
if len(result) == 0:
    print("PREDAJA")
else:
    print("".join(sorted(result)))

#https://www.acmicpc.net/problem/1225
a, b = map(str, input().split())
result = 0
for i in range(0, len(a)):
    for r in range(0, len(b)):
        result += int(a[i]) * int(b[r])
print(result)