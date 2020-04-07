import itertools

N = int(input())
S = input()


def solve():
    cnt = 0
    for key in itertools.groupby(S):
        cnt += 1

    return cnt


print(solve())
