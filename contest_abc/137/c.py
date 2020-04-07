from collections import Counter


def solve(s):
    c = Counter(s)

    ans = 0
    for i in c.values():
        ans += i * (i - 1) // 2

    return ans


n = int(input())
s = []

for i in range(n):
    tmp = sorted(input())
    s.append("".join(tmp))

print(solve(s))
