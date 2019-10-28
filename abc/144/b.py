N = int(input())


def solve(N):
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                return 'Yes'

    return 'No'


print(solve(N))
