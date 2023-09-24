N = int(input())
ans = 0

for i in range(N):
    one, sign, two = map(str, input().split())
    if sign == "+":
        ans += int(one) + int(two)
    elif sign == "-":
        ans += int(one) - int(two)
    elif sign == "*":
        ans += int(one) * int(two)
    elif sign == "/":
        ans += int(one) // int(two)
print(ans)