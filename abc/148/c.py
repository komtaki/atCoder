import fractions

A, B = map(int, input().split())


def solve():
    return print(A * B // fractions.gcd(A, B))


solve()
