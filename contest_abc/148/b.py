N = int(input())
S, T = map(str, input().split())


def solve():
    answer = ''
    for i in range(N):
        answer += (S[i] + T[i])
    return print(answer)


solve()
