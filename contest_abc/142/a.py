def filter_odd(x):
    return x % 2 == 1


def solve(N):
    odd_list = list(
        filter(filter_odd, range(1, N + 1)[::-1])
    )
    return len(odd_list) / N


N = int(input())

print(solve(N))
