#
import sys

b = int(input())
reli = []
li = []
for i in range(0, b):
    a = input()
    li.append(a)
    reli.append([])
for i in range(0, b):
    for r in range(0, b):
        if li[i][r] != '.':
            reli[i].append('*')
        else:
            reli[i].append(0)

for i in range(0, b):
    for r in range(0, b):
        if li[i][r] != '.':
            if i-1 > -1 and r-1 > -1 and reli[i-1][r-1] != '*':
                reli[i-1][r-1] += int(li[i][r])
            if i-1 > -1 and reli[i-1][r] != '*':
                reli[i-1][r] += int(li[i][r])
            if r-1 > -1 and reli[i][r-1] != '*':
                reli[i][r-1] += int(li[i][r])
            if i+1 < b and r+1 < b and reli[i+1][r+1] != '*':
                reli[i+1][r+1] += int(li[i][r])
            if i-1 > -1 and r+1 < b and reli[i-1][r+1] != '*':
                reli[i-1][r+1] += int(li[i][r])
            if r+1 < b and reli[i][r+1] != '*':
                reli[i][r+1] += int(li[i][r])
            if i+1 < b and reli[i+1][r] != '*':
                reli[i+1][r] += int(li[i][r])
            if i+1 < b and r-1 > -1 and reli[i+1][r-1] != '*':
                reli[i+1][r-1] += int(li[i][r])
for i in range(0, b):
    for r in range(0, b):
        if reli[i][r] != '*' and reli[i][r] > 9:
            print("M", end = "")
        else:
            print(reli[i][r], end = "")
    print()