# import itertools
# import math
import fractions

MOD = 10 ** 9 + 7


def solve(N, A):
    lcm_ans = A[0]
    for i in range(1, N):
        lcm_ans = lcm_ans * A[i] // fractions.gcd(lcm_ans, A[i])

    ans = 0
    for AA in A:
        ans += lcm_ans // AA

    return ans % MOD


N = int(input())
# S = input()
# A, B = map(int, input().split())
A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(N, A))
