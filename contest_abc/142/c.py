N = int(input())
A = [int(i) for i in input().split()]

dic = dict(zip(range(1, N + 1), A))

sort_dic = sorted(dic.items(), key=lambda x:x[1])

for i in sort_dic:
    print(i[0], end = ' ')
