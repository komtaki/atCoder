import fractions


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


def solve():
    a, b, c, d = map(int, input().split())
    a = a - 1

    c_a = a // c
    c_b = b // c

    d_a = a // d
    d_b = b // d

    lcm = lcm(min(c, d), max(c, d))

    l_a = a // lcm
    l_b = b // lcm

    return (b - a) - (c_b - c_a) - (d_b - d_a) + (l_b - l_a)


print(solve())
