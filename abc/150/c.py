import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


answer = list(range(1, N + 1))


def solve(temp):
    index = 0
    for group in itertools.permutations(answer, N):
        if list(group) == temp:
            return index
        index += 1


answer = solve(P) - solve(Q)

print(max(answer, -answer))
