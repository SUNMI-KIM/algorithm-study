#https://www.acmicpc.net/problem/3474
import sys

def count_factor(n, factor):
    count = 0
    div = factor
    while n >= div:
        count += n // div
        div *= factor
    return count

T = int(sys.stdin.readline())

for i in range(0, T):
    N = int(sys.stdin.readline())
    print(count_factor(N, 5))