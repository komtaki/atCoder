A, B = map(int, input().split())


def solve(A, B):
    sockets = 1
    taps = 0
    while sockets < B:
        sockets -= 1
        sockets += A
        taps += 1

    return taps


print(solve(A, B))
