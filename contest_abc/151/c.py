# import itertools
# import math

# N = int(input())
# S = input()
N, M = map(int, input().split())
# A = list(map(int, input().split()))

ans_p = [0] * N
ans_s = [0] * N

for i in range(M):
    input_sp = input().split()
    P = int(input_sp[0]) - 1
    S = input_sp[1]

    if S == 'AC':
        ans_s[P] = 1
    elif S == 'WA' and ans_s[P] == 0:
        ans_p[P] += 1

for i in range(len(ans_p)):
    if ans_s[i] == 0 and ans_p[i] != 0:
        ans_p[i] = 0

print(str(sum(ans_s)) + " " + str(sum(ans_p)))
