def resolve():
    A, B, C = map(int, input().split())

    if A == B and B == C:
        print('No')
        return

    if A == B or B == C or A == C:
        print('Yes')
        return

    print('No')


resolve()
