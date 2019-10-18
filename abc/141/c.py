N, K, Q = map(int, input().split())
A = [int(input()) for i in range(Q)]


def is_winner(point):
    return 'Yes' if point > 0 else 'No'


def solve():
    points = [K-Q] * N

    for answer_id in A:
        answer_id -= 1
        points[answer_id] += 1

    return '\n'.join(list(map(is_winner, points)))


print(solve())
