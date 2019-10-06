# https://atcoder.jp/contests/agc039/tasks/agc039_a
import sys


def input():
    return sys.stdin.readline().strip().decode('utf-8')


S = input()
K = int(input())
t = ''

for i in range(1, K + 1):
    t = t + S

t = list(t)
replace_count = 0
replace_word = '#'

for i in range(1, len(t) + 1):
    before_index = i - 1

    if t[before_index] != replace_word and t[before_index] == t[i]:
        replace_count += 1
        t[i] = replace_word


print(replace_count)
