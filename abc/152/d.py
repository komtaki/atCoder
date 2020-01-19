# import itertools
# import math

aa = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 7],
    [8, 8],
    [9, 9],

    [11, 11],
    [22, 22],

    [1, 11],
    [2, 22],

    [11, 1],
    [12, 21],

    [21, 12],
    [22, 2],
]


def solve(N):
    if N < 10:
        return N

    size = len(str(N))
    max_place = int(str(N)[0])

    ans = 0
    ans += 9 * (size - 1)

    for i in range(size):
        ans += max_place * size

    return ans


N = int(input())
# S = input()
# A, B = map(int, input().split())
# A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(N))
