N = int(input())
A = list(map(int, input().split()))


def solve():
    if A.count(1) == 0:
        return print(-1)

    number_possible = 1

    for i in range(N):
        if A[i] == number_possible:
            number_possible += 1

    return print(N - number_possible + 1)


solve()
