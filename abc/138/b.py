n = int(input())
a = map(int, input().split())


def solve():
    ans_tmp = 0
    for aa in a:
        ans_tmp = ans_tmp + 1 / aa

    return 1 / ans_tmp


print(solve())
