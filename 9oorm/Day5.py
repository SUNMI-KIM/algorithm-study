#이진 수 변환 함수
def binary_count(binary):
    count = 0
    while binary > 0:
        count += binary % 2
        binary //= 2
    return count


N, K = map(int, input().split())
l = []
for element in list(map(int, input().split())):
    l.append([binary_count(element), element])

l.sort()
print(l)
print(l[N - K][1])