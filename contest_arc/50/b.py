R, B = map(int, input().split())
x, y = map(int, input().split())


def check(k):  # kが解として適しているかをチェックする
    r = R - k
    b = B - k
    if r < 0 or b < 0:
        return False
    if r // (x - 1) + b // (y - 1) < k:
        return False
    return True


# 二分探索で答えを探す
def solve():
    ok = 0
    ng = max(R, B)

    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    return ok


if x == 1 or y == 1:
    print(min(R, B))
    exit()


print(solve())
