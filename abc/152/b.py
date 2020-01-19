# import itertools
# import math


def solve(A, B):
    AA = ''
    for b in range(B):
        AA += str(A)

    BB = ''
    for a in range(A):
        BB += str(B)
    ans = sorted([AA, BB])
    return ans[0]


# N = int(input())
# S = input()
A, B = map(int, input().split())
# A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(A, B))
