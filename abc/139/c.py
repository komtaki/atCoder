N = int(input())
H = [map(int, input().split())]


def solve(N, H):
    ans = 0
    val = 0

    for i in range(N):
        if H[i] >= H[i+1]:
            val += 1
        else:
            val = 0
        ans = max(val, ans)

    return ans


print(solve(N, H))
