def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    unique = len(list(set(A)))

    if len(A) == unique:
        print('YES')
        return

    print('NO')


resolve()
