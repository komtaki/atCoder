import itertools

N = int(input())
L = [int(i) for i in input().split()]


def solve():
    pattern_cnt = 0

    for pattern in list(itertools.combinations(L, 3)):
        if (pattern[0] < pattern[1] + pattern[2]) and (pattern[2] < pattern[0] + pattern[1]) and  (pattern[1] < pattern[0] + pattern[2]):
            pattern_cnt += 1

    return pattern_cnt


print(solve())