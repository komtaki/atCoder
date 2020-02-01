import sys
input = sys.stdin.readline


def solve(N, A, B):
    defeat_monstar = 0
    for nn in range(N):
        # 最初の街のモンスターのみ倒せる場合
        if A[nn] >= B[nn]:
            defeat_monstar += B[nn]
        else:
            B[nn] -= A[nn]
            # 次の街のモンスターも全て倒せる場合
            if A[nn + 1] <= B[nn]:
                defeat_monstar += A[nn] + A[nn + 1]
                A[nn + 1] = 0
            else:
                A[nn + 1] = A[nn + 1] - B[nn]
                defeat_monstar += A[nn] + B[nn]

    return defeat_monstar


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(solve(N, A, B))
