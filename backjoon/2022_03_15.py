#https://www.acmicpc.net/problem/2789
a = input()
print(a.replace("C", "").replace("A", "").replace("M", "").replace("B", "").replace("R", "").replace("I", "").replace("D", "").replace("G", "").replace("E", ""))

#https://www.acmicpc.net/problem/2475
import sys
a = sys.stdin.readline().split()
sum = 0
for i in range(0, len(a)):
    sum += int(a[i]) ** 2
print(sum%10)

#https://www.acmicpc.net/problem/2822
import sys
li = []
for i in range(0, 8):
    a = int(sys.stdin.readline())
    li.append(a)
li_sort = sorted(li)
li_index = []
sum = 0
for i in range(7, 2, -1):
    sum += li_sort[i]
    li_index.append(str(li.index(li_sort[i]) + 1))
print(sum)
li_index = sorted(li_index)
print(" ".join(li_index))

#https://www.acmicpc.net/problem/1094
# 이진법으로 나타내서 각자리에 1이 얼마나 있는지 보기
a = str(bin(int(input())))
b = len(a)
result = 0
for i in range(2, b):
    if a[i] == "1":
        result += 1
print(result)

#https://www.acmicpc.net/problem/1264
a = input()
b = len(a)
li = []
while True:
    result = 0
    if a == '#':
        break
    for i in range(0, b):
        if a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u" or a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U" :
            result += 1
    li.append(result)
    a = input()
    b = len(a)
for i in range(0, len(li)):
    print(li[i])

#https://www.acmicpc.net/problem/1568
a = int(input())
n = 1
nn = 0
while a != 0:
    if a < n:
        n = 1
    else: 
        a = a - n
        n += 1
        nn += 1
print(nn)

#https://www.acmicpc.net/problem/1864
a = input()
b = len(a)
li = []
dic = {"-": 0, "\\": 1, "(": 2, "@": 3, "?": 4, ">": 5, "&": 6, "%": 7, "/": -1}
while True:
    sum = 0
    if a == "#":
        break
    for i in range(0, b):
        sum += dic[a[i]] * (8 ** (b-1-i))
    li.append(sum)
    a = input()
    b = len(a)
for i in range(0, len(li)):
    print(li[i])