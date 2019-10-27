N, K = map(int, input().split())
s = input()

RL = s.count('RL')
LR = s.count('LR')
diff = RL + LR

cnt = (N-1) - diff

for i in range(K):
    if diff >= 2:
        diff -= 2
        cnt += 2
    elif diff == 1:
        diff -= 1
        cnt += 1

print(cnt)
