from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)

H, N = map(int, input().split())

AB = []
for i in range(N):
    A, B = map(int, input().split())
    AB.append((A, B))

AB.sort(key=lambda ab: (ab[0] / ab[1], -ab[0]), reverse=True)


@lru_cache(maxsize=None)
def solve(h):
    if h <= 0:
        return 0
    best = float("inf")
    for a, b in AB:
        val = b + solve(h - a)
        if val < best:
            best = val
        else:
            break
    return best


print(solve(H))
