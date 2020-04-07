# import itertools
# import math


def solve(N, K, H):
    H.sort(reverse=True)
    if N <= K:
        return 0

    for i in range(K):
        H[i] = 0
    return sum(H)


# N = int(input())
# S = input()
N, K = map(int, input().split())
H = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(N, K, H))
