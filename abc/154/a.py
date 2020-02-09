def resolve():
    S, T = map(str, input().split())
    A, B = map(int, input().split())
    U = input()

    if S == U:
        A -= 1
        print(str(A) + ' ' + str(B))
        return
    B -= 1
    print(str(A) + ' ' + str(B))


resolve()
