A, B = (int(x) for x in input().split())


def solve():
    if A < B * 2:
        return 0

    return A - B * 2


print(solve())
