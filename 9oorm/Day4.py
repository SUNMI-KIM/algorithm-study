'''def ascending(i):
    if k[i + 1] - k[i] >= 0:
        return True
    return False

def descending(i):
    if k[i + 1] - k[i] <= 0:
        return True
    return False

N = int(input())
k = list(map(int, input().split()))
max_value = max(k)

for i in range(N - 1):
    if k[i] == max_value:
        for r in range(i + 1, N - 1):
            if not descending(r):
                print(0)
                exit()
        break

    if not ascending(i):
        print(0)
        exit()
print(sum(k))'''

def ascending(middle):
    for i in range(0, middle):
        if k[i + 1] - k[i] < 0:
            print(0)
            exit()

def descending(middle):
    for i in range(middle, N - 1):
        if k[i + 1] - k[i] > 0:
            print(0)
            return exit()

N = int(input())
k = list(map(int, input().split()))
middle = k.index(max(k))

ascending(middle)
descending(middle)
print(sum(k))

