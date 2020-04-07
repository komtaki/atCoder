# import itertools
# import math


def solve(X, A):
    return 10 if X >= A else 0


# N = int(input())
# S = input()
X, A = map(int, input().split())
# A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(X, A))
