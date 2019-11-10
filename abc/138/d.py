n, q = map(int, input().split())
ki = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())
    ki[b] = a

c = [0] * (n + 1)
for i in range(q):
    p, x = map(int, input().split())
    c[p] += x


def solve():
    for i in range(1, n + 1):
        c[i] += c[ki[i]]

    return " ".join(map(str, c[1:]))


print(solve())
