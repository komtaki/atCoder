def prepare(n, MOD):
    # n! の計算
    f = 1
    for m in range(1, n + 1):
        f *= m
        f %= MOD
    fn = f

    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return fn, invs


def ncr(n, r, invs, MOD):
    ret = invs[r]
    for i in range(n, n - r, -1):
        ret = ret * i % MOD
    return ret


MOD = 10 ** 9 + 7

n, b = list(map(int, input().split()))
fn, invs = prepare(b, MOD)
ans = ncr(n, b, invs, MOD)

print(ans)
