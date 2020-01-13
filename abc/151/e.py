# import itertools
# import math

MOD = 10 ** 9 + 7


def solve(N, K, A):
    if K == 1:
        return 0

    sorted_a = A.sorted()
    half_N = len(sorted_a) // 2

    if half_N =< K:
        for i in range(half_N):
            

    return


# N = int(input())
# S = input()
N, K = map(int, input().split())
A = list(map(int, input().split()))

print(solve(N, K, A))
