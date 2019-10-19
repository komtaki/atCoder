n = int(input())
a = [float("inf")] * n
b = list(map(int, input().split()))


def solve():
    for i in range(n - 1):
        a[i] = min(a[i], b[i])
        a[i + 1] = min(a[i + 1], b[i])

    return sum(a)


print(solve())
