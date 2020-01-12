
def solve(N, H):
    ans = 0
    val = 0

    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            val += 1
        else:
            val = 0

        ans = max(val, ans)

    return ans


N = int(input())
H = list(map(int, input().split()))

print(solve(N, H))
