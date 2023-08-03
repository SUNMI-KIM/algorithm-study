#https://www.acmicpc.net/problem/2857
li = []
for i in range(0, 5):
    b = input()
    if b.count("FBI") >= 1:
        li.append(i+1)
if len(li) == 0 :
    print("HE GOT AWAY!")
else:
    for i in li:
        print(i)

#https://www.acmicpc.net/problem/2947
li = input().split()
i = 0
while True:
    if li == sorted(li):
        break
    elif li[i] > li[i+1]:
        li[i], li[i+1] = li[i+1], li[i]
        print(" ".join(li))
    i += 1
    if i >= 4:
        i = 0

#https://www.acmicpc.net/problem/2953
li = []
for i in range(0, 5):
    a = list(map(int, input().split()))
    li.append(sum(a))
print(str(li.index(max(li))+1) + " " + str(max(li)))

#https://www.acmicpc.net/problem/2966
dic = {"Adrian" : 0, "Bruno" : 0, "Goran" : 0}
a = int(input())

Adrian = "ABC" * (a//3 + 1)
Bruno = "BABC" * (a//4 + 1)
Goran = "CCAABB" * (a//6 + 1)

b = input()
for i in range(0, a):
    if b[i] == Adrian[i]:
        dic["Adrian"] += 1
    if b[i] == Bruno[i]:
        dic["Bruno"] += 1
    if b[i] == Goran[i]:
        dic["Goran"] += 1
c = [k for k, v in dic.items() if max(dic.values()) == v]
print(max(dic.values()))
for i in range(0, len(c)):
    print(c[i])


