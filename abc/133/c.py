L, R = map(int, input().split())
M = 2019


def solve():
    if (R - L) > M:
        return 0

    m = M
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            if (i * j) % M < m:
                m = (i * j) % M
    return m


print(solve())
