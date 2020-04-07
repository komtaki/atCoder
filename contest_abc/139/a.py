S = input()
T = input()


def solve(S, T):
    cnt = 0
    for i in range(0, 3):
        if S[i] == T[i]:
            cnt += 1

    return cnt


print(solve(S, T))
