import heapq


def solve(n, v):
    heapq.heapify(v)

    while len(v) != 1:
        x = heapq.heappop(v)
        y = heapq.heappop(v)
        z = (x + y) / 2
        heapq.heappush(v, z)

    return v[0]


n = int(input())
v = list(map(int, input().split()))

print(solve(n, v))
