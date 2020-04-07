import itertools

S = input()


def solve():
    ans = []
    ss = itertools.groupby(S)

    for key, groups in ss:
        groups = list(groups)
        groups_cnt = len(groups)
        nothing_group = [0] * (groups_cnt - 1)

        even_cnt = groups_cnt // 2
        odd_cnt = groups_cnt - even_cnt

        if key == 'R':
            tmp_ans = nothing_group + [odd_cnt]
            tmp_ans.append(even_cnt)
        elif key == 'L':
            ans[-1] += odd_cnt
            ans[-2] += even_cnt
            tmp_ans = nothing_group

        ans += tmp_ans

    print(*ans)


solve()
