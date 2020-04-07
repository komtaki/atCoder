import itertools
import math

n = int(input())
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())


def solve():
    patterns = list(itertools.permutations(range(n)))

    sum_ans = []

    for pattern in patterns:
        tmp_ans = []
        for j in range(n - 1):
            now_city = pattern[j]
            next_city = pattern[j + 1]
            tmp = (x[now_city] - x[next_city]) ** 2 + (y[now_city] - y[next_city]) ** 2
            tmp_ans.append(
                math.sqrt(tmp)
            )
        sum_ans.append(
            sum(tmp_ans)
        )

    return sum(sum_ans) / len(patterns)


print(solve())
