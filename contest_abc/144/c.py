N = int(input())


def solve(n):
    i = 1
    ans = N - 1
    while i * i <= n:
        ans_tmp = ((N // i) - 1) + (i - 1)
        if n % i == 0 and ans > ans_tmp:
            ans = ans_tmp
        i += 1
    return ans


print(solve(N))
