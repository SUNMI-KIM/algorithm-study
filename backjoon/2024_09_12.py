#https://www.acmicpc.net/problem/4779

def solve(N, answer, start, end):
    if N == 0:
        return

    for i in range(start + (end-start)//3, start + (end-start)//3 * 2):
        answer[i] = 0
    
    solve(N - 1, answer, start, start + (end-start)//3)
    solve(N - 1, answer, start + (end-start)//3 * 2, end)

while True:
    try:
        N = int(input())
        answer = [1 for i in range(pow(3, N))]
        solve(N, answer, 0, pow(3, N))
        for i in answer:
            if i == 1:
                print("-", end = "")
            else:
                print(" ", end = "")
        print()
    except: break