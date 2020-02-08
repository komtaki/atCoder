import numpy as np

h, n = map(int, input().split())
ab = np.array([list(map(int, input().split()))for _ in range(n)])

a, b = ab[:, 0], ab[:, 1]

dp = np.zeros(h + 1, dtype=np.int)
for i in range(1, h + 1):
    tmp = dp[np.maximum(i - a, 0)]
    tmp += b
    dp[i] = np.min(tmp)

print(dp[h])
