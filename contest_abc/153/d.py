def solve(H):
    ans_attack = 0
    hp = H
    enemy = 1

    while hp > 1:
        hp = hp // 2
        ans_attack = ans_attack + enemy
        enemy = enemy * 2

    return ans_attack + enemy


H = int(input())

print(solve(H))
