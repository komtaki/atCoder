def solve(s):
    weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    ans = len(weekday) - (weekday.index(s) + 1)
    return ans if ans != 0 else 7


S = input()

print(solve(S))
