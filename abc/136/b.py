# import itertools


def solve(N):
    ans = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 == 1:
            ans += 1
    return ans


N = int(input())
# S = input()
# A, B = map(int, input().split())
# A = list(map(int, input().split()))

# P = []
# S = []
# for i in range(N):
#     pp, ss  = map(int, input().split())
#     P.append(pp)
#     S.append(ss)

print(solve(N))
