# import itertools
import math

import sys
input = sys.stdin.readline


def solve(N, D):
    return math.ceil(N / ((D * 2) + 1))


# N = int(input())
# S = input()
N, D = map(int, input().split())
# A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(N, D))
