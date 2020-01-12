# import itertools
import math


def check(A, B, X, mid):  # kが解として適しているかをチェックする
    data_size = int(math.log10(mid) + 1)
    return ((A * mid) + (B * data_size)) <= X


MAX = 1000000000


# 二分探索で答えを探す
def solve(A, B, X):
    if (A + B) > X:
        return 0
    elif ((A * MAX) + (B * int(math.log10(MAX) + 1))) <= X:
        return MAX

    ok = 0
    ng = MAX

    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if check(A, B, X, mid):
            ok = mid
        else:
            ng = mid

    return ok


# N = int(input())
# S = input()
A, B, X = map(int, input().split())
# A = list(map(int, input().split()))

print(solve(A, B, X))
