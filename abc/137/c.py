from collections import Counter

n = int(input())
s = [sorted(input()) for i in range(n)]

c = Counter(["".join(s[i]) for i in range(n)])

ans = 0
for i in c.values():
    ans += i * (i - 1) // 2

print(ans)
