from collections import Counter


def solve(n, ddd):
    if ddd[0] != 0:
        return 0

    cnt = Counter(ddd)

    if cnt[0] != 1:
        return 0

    max_c = max(cnt)
    for i in range(max_c + 1):
        if i not in cnt:
            return 0

    MOD = 998244353
    ans = 1

    for i in range(max_c):
        prev = cnt[i]
        curr = cnt[i + 1]
        ans = ans * pow(prev, curr, MOD) % MOD
    return ans


n = int(input())
ddd = list(map(int, input().split()))

print(solve(n, ddd))
