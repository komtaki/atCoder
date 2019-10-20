import bisect

n = int(input())
li = list(map(int, input().split()))
ans = 0

li.sort()

for i in range(n):
    for j in range(i+1, n):
        cnt = bisect.bisect_left(li, li[i]+li[j])

        ans += cnt - j - 1

print(ans)
