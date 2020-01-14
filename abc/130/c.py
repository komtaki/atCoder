# import itertools
# import math


def solve(W, H, x, y):
    area = W * H
    half_line_count = 0
    if (W / 2) == x and (H / 2) == y:
        half_line_count = 1
    return [area / 2, half_line_count]


# N = int(input())
# S = input()
W, H, x, y = map(int, input().split())
# A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(*solve(W, H, x, y))
