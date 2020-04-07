# import itertools
# import math


def solve(H, N, A):
    if (sum(A) >= H):
        return 'Yes'
    return 'No'


# N = int(input())
# S = input()
H, N = map(int, input().split())
A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(H, N, A))
