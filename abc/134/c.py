# import itertools
# import math

import sys
input = sys.stdin.readline


def solve(N, A):
    max_idx = A.index(max(A))
    s = sorted(A, reverse=True)

    for i in range(N):
        if i == max_idx:
            print(s[1])
        else:
            print(s[0])


N = int(input())
# S = input()
# A, B = map(int, input().split())
# A = list(map(int, input().split()))


A = []
for i in range(N):
    aa = int(input())
    A.append(aa)


solve(N, A)
