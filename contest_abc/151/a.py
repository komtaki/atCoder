# import itertools
# import math


def solve(S):
    alp = [chr(i) for i in range(97, 97+26)]
    index = alp.index(S) + 1
    if index == len(alp):
        index = 0
    return alp[index]


# N = int(input())
S = input()
# A, B = map(int, input().split())
# A = list(map(int, input().split()))

print(solve(S))
