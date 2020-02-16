import collections


def resolve():
    N = int(input())
    S = []
    for i in range(N):
        ss = input()
        S.append(ss)

    counter = collections.Counter(S)
    _, max_count = counter.most_common()[0]

    ans = []
    for key in counter:
        if (counter[key] == max_count):
            ans.append(key)

    ans.sort()

    for a in ans:
        print(a)


resolve()
