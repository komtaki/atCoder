# import itertools
# import math


def solve(N, P):
    if P[0] == 1:
        return 1
    ans = [P[0]]

    for i in range(1, N):
        if ans[-1] > P[i]:
            ans.append(P[i])

    return len(ans)


N = int(input())
# S = input()
# A, B = map(int, input().split())
P = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(N, P))
