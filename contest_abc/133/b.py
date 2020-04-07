from math import sqrt


import sys
input = sys.stdin.readline


def solve(N, D, X):
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            dist = sqrt(sum((X[i][d] - X[j][d])**2 for d in range(D)))
            if dist == int(dist):
                ans += 1

    return ans


# N = int(input())
# S = input()
N, D = map(int, input().split())
# A = list(map(int, input().split()))

X = []
for i in range(N):
    X.append(
        list(map(int, input().split()))
    )

print(solve(N, D, X))
