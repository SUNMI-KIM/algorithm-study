#https://www.acmicpc.net/problem/1735
import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

result1 = a * d + b * c
result2 = b * d
cd = gcd(result1, result2)
print(result1 // cd, result2 // cd)