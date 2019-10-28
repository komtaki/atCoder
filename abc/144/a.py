A, B = map(int, input().split())


def solve(A, B):
    if A > 9 or B > 9:
        return -1

    return A * B


print(solve(A, B))
