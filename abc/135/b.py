# import itertools
# import math

import sys
input = sys.stdin.readline


def solve(N, P):
    NN = sorted(N)
    cnt = 0
    for l1, l2 in zip(N, NN):
        if l1 != l2:
            cnt += 1

    return 'YES' if cnt <= 2 else 'NO'


N = int(input())
# S = input()
# A, B = map(int, input().split())
P = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(N, P))
