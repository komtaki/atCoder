# import itertools
# import math

import sys
input = sys.stdin.readline


def solve(A, B):
    K = (A + B) / 2
    if int(K) == K:
        return int(K)
    return 'IMPOSSIBLE'


# N = int(input())
# S = input()
A, B = map(int, input().split())
# A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(A, B))
