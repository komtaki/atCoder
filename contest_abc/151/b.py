# import itertools
# import math


def solve(N, K, M, A):
    X = (M * N) - sum(A)

    if X > K:
        X = -1
    elif X < 0:
        X = 0
    return X


# N = int(input())
# S = input()
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

print(solve(N, K, M, A))
