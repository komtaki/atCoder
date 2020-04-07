S = input()


def solve(S):
    index = 1
    for word in S:
        if index % 2 != 0 and word == 'L':
            return 'No'
        elif index % 2 == 0 and word == 'R':
            return 'No'
        index += 1

    return 'Yes'


print(solve())
