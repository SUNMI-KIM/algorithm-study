#https://www.acmicpc.net/submit/10950
a = int(input())
int_list = []
for i in range(0, a):
    c, b = map(int, input().split())
    int_list.append(c + b)
for i in range(len(int_list)):
    print(int_list[i])

#https://www.acmicpc.net/problem/11022
a = int(input())
int_list = []
for i in range(0, a):
    c, b = map(int, input().split())
    int_list.append("Case #%d: %d + %d = %d" % (i + 1, c, b, c + b))
for i in range(len(int_list)):
    print(int_list[i])

#https://www.acmicpc.net/problem/10952
int_list = []
c, b = map(int, input().split())
while c != 0 and b != 0:
    int_list.append(c + b)
    c, b = map(int, input().split())
for i in range(len(int_list)):
    print(int_list[i])

#https://www.acmicpc.net/problem/13410
c, b = map(int, input().split())
int_list = []
for i in range(1, b + 1):
    result = str(c * i)
    result = result[::-1]
    int_list.append(int(result))
print(max(int_list))

#https://www.acmicpc.net/problem/1110
a = str(input())
a_same = a
int_b = 0
score = 0
while True:
    if int(a) == 0 :
        print(1)
        break
    elif int(a) < 10:
        a = "0" + a

    int_b = int(a[0]) + int(a[1])
    score += 1

    if int_b < 10 :
        a = a[1] + str(int_b)
    elif int_b >= 10 :
        a = a[1] + str(int_b)[1]
    
    if a[0] == '0':
        a = a[1]

    if a == a_same :
        print(score)
        break
    
#https://www.acmicpc.net/problem/10871
c, b = map(int, input().split())
a = input()
int_list = a.split()
result_list = []
for i in range(0, c):
    if int(int_list[i]) < b:
        result_list.append(int_list[i])
print(' '.join(result_list))

#https://www.acmicpc.net/problem/10818
a = input()
b = input()
int_list = b.split(" ")
map_intlist = list(map(int, int_list))
return_max = max(map_intlist)
return_min = min(map_intlist)
print(return_min, return_max)

#https://www.acmicpc.net/problem/1302
a = int(input())
dic = {}
for i in range(0, a):
    b = input()
    if b not in dic:
        dic[b] = 1
    else :
        dic[b] += dic[b]
dic = dict(sorted(dic.items()))
max_result = max(dic, key=dic.get)
print(max_result)

#https://www.acmicpc.net/problem/2562
b = []
for i in range(0, 9):
    a = int(input())
    b.append(a)
max_value = max(b)
max_value_순서 = b.index(max_value)
print(max_value)
print(max_value_순서 + 1)

#https://www.acmicpc.net/problem/3052
dic = []
for i in range(0, 10):
    a = int(input())
    b = a % 42
    if b not in dic:
        dic.append(b)
print(len(dic))
