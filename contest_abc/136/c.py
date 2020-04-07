# import itertools
# import math


def solve(N, H):
    for i in range(N - 1):
        if H[i] < H[i+1]:
            H[i+1] -= 1
        elif H[i] > H[i+1]:
            return 'No'
    return 'Yes'


N = int(input())
# S = input()
# A, B = map(int, input().split())
H = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(N, H))
