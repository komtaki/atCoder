A, B, K = map(int, input().split())


def solve():
    if ((A - K) > 0):
        return [A - K, B]
    ans = B - (K - A)
    return [0,  max(0, ans)]


print(*solve())
