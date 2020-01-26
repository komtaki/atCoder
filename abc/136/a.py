# import itertools
# import math


def solve(A, B, C):
    ans = A - B - C
    if ans < 0:
        ans = abs(ans)
    else:
        ans = 0
    return ans


# N = int(input())
# S = input()
A, B, C = map(int, input().split())
# A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(A, B, C))
