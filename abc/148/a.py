A = int(input())
B = int(input())


def solve():
    answer = [1, 2, 3]
    answer.remove(A)
    answer.remove(B)

    return print(answer[0])


solve()
