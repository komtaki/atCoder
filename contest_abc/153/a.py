# import itertools
# import math


def solve(H, A):
    ans = H // A
    if H % A != 0:
        ans += 1
    return ans


# N = int(input())
# S = input()
H, A = map(int, input().split())
# A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(H, A))
