#https://www.acmicpc.net/problem/1541
import sys
import re

form = re.split('([+-])', sys.stdin.readline().strip())

ans = int(form[0])
for i in range(1, len(form)):
    if form[i] == '-':
        index = i + 1
        while index < len(form):
            if form[index] != '-' and form[index] != '+':
                ans -= int(form[index])
            index += 1
        break
    if form[i] != '+':
        ans += int(form[i])
print(ans)