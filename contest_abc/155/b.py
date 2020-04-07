def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    even = list(filter(lambda x: x % 2 == 0, A))

    for ee in even:
        if (ee % 3) != 0 and (ee % 5) != 0:
            print('DENIED')
            return

    print('APPROVED')


resolve()
