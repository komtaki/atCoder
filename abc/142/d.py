from math import gcd

A, B = map(int, input().split())


def solve(A, B):
    g = gcd(A, B)
    return len(set(prime_factorize(g)))


def prime_factorize(n):
    a = [1]
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


print(solve(A, B))
