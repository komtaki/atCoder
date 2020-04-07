import sys
input = sys.stdin.readline


def solve(N, P):
    PP = sorted(P)
    cnt = 0
    for l1, l2 in zip(P, PP):
        if l1 != l2:
            cnt += 1

    return 'YES' if cnt <= 2 else 'NO'


N = int(input())
P = list(map(int, input().split()))

print(solve(N, P))
