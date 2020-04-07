# import itertools
# import math


def solve(N, X, L):
    ans = 1
    now = 0
    for ll in L:
        now += ll
        if now <= X:
            ans += 1
    return ans


# N = int(input())
# S = input()
N, X = map(int, input().split())
L = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(N, X, L))
