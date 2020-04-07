n = int(input())
s = input()


def solve():
    if n % 2 != 0:
        return 'No'

    half_length = n // 2

    if s[:half_length] == s[half_length:]:
        return 'Yes'

    return ' No'


print(solve())
