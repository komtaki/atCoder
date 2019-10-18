N, K = (int(x) for x in input().split())
H = [int(i) for i in input().split()]


def filter_height_by_K(x):
    return x >= K


def solve(N, H):
    ride_list = list(
        filter(filter_height_by_K, H)
    )
    return len(ride_list)


print(solve(N, H))
