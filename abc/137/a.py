a, b = map(int, input().split())


def solve():
    plus = a + b
    minus = a - b
    multi = a * b

    return max(plus, minus, multi)


print(solve())
