k, x = map(int, input().split())


def solve():
    min_ans = (x - k + 1)
    max_ans = (x + k)

    return ' '.join(
        map(str, range(min_ans, max_ans))
    )


print(solve())
