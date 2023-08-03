#https://www.acmicpc.net/problem/2576
li = []
for i in range(0, 7):
    a = int(input())
    if a % 2 != 0:
        li.append(a)
li.sort()
if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(li[0])

#https://www.acmicpc.net/problem/2490
import sys

for i in range(0, 3):
    a = sys.stdin.readline().split()
    if a.count("1") == 3:
        print("A")
    elif a.count("1") == 2:
        print("B")
    elif a.count("1") == 1:
        print("C")
    elif a.count("1") == 0:
        print("D")
    else:
        print("E")

#https://www.acmicpc.net/problem/2566
import sys
c = 0
for i in range(0, 9):
    a = sys.stdin.readline().split()
    b = max(a)
    if int(max(a)) > int(c):
        c = max(a)
        d = i + 1
        e = a.index(c)
print(c)
print(str(d) + " " + str(e + 1))

#https://www.acmicpc.net/problem/2744
a = input()
b = ""
for i in range(0, len(a)):
    if a[i].isupper():
        b += a[i].lower()

    else:
        b += a[i].upper()
print(b)

#https://www.acmicpc.net/problem/2754
dic = {"A+" : 4.3, "A0" : 4.0, "A-" : 3.7,
        "B+" : 3.3, "B0" : 3.0, "B-" : 2.7,
        "C+" : 2.3, "C0" : 2.0, "C-" : 1.7,
        "D+" : 1.3, "D0" : 1.0, "D-" : 0.7,
        "F" : 0.0}
a = input()
print(dic[a])

#https://www.acmicpc.net/problem/2846
a = int(input())
b = input().split()
li = []
c = 0
for i in range(0, a-1):
    if int(b[i]) < int(b[i+1]):
        c += (int(b[i+1]) - int(b[i]))
    else:
        li.append(c)
        c = 0
li.append(c)
print(max(li))