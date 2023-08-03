#https://www.acmicpc.net/problem/10773
a = int(input(""))
li = []
for i in range(0, a):
    b = int(input())
    if b != 0:
        li.append(b)
    elif b == 0 :
        li.pop()
print(sum(li))

#https://www.acmicpc.net/problem/2750
a = int(input())
li = []
for i in range(0, a):
    b = int(input())
    li.append(b)
li_sort = sorted(li)
for i in range(0, a):
    print(li_sort[i])

#https://www.acmicpc.net/problem/2711
a = int(input())
li = []
for i in range(0, a):
    b = input()
    b_li = b.split()
    c = int(b_li[0])
    li.append(b_li[1][:c-1] + b_li[1][c:])
for i in range(0, a):
    print(li[i])