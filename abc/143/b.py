import itertools

N = int(input())
D = [int(i) for i in input().split()]


def solve():
    point = 0

    for pattern in list(itertools.combinations(D, 2)):
        point += pattern[0] * pattern[1]

    return point


print(solve())
