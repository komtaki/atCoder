# import itertools
# import math
import numpy as np


H, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()

ans = 0
dp = np.zeros(H, dtype=int)
for a, b in AB:
    ans = max(ans, dp.max() + b)
    np.max(dp[:-a] + b, dp[a:], out=dp[a:])

print(ans)
+
