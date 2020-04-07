# https://atcoder.jp/contests/agc039/tasks/agc039_a
import sys


def input():
    return sys.stdin.readline().strip().decode('utf-8')


S = 'isiii'  # input()
K = 4  # int(input())

isiii / isiii / isiii / isiii

isiii

1 * 4 - ((1 / 2) + (3 / 2) - (1 + 3 / 2)) * (4 - 1)

# for i in range(1, K + 1):
#     t = t + S

t = list(K)
replace_count = 0
REPLACE_WORD = '#'

for i in range(1, len(t) + 1):
    before_index = i - 1

    if t[before_index] != REPLACE_WORD and t[before_index] == t[i]:
        replace_count += 1
        t[i] = REPLACE_WORD


def search_same_word_cnt(word, ):
    for i in range(1, len(t) + 1):


if t[0] == t[len(t) - 1]:
    answer = replace_count * K - ()
else:
    answer = replace_count * K

print(answer)
