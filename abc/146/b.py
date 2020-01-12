def solve(N, S):
    alp = [chr(i) for i in range(65, 65+26)]
    new_text = ''

    for i in range(len(S)):
        new_char_i = alp.index(S[i]) + N

        if new_char_i >= len(alp):
            new_char_i -= len(alp)

        new_text += alp[new_char_i]

    return new_text


N = int(input())
S = input()

print(solve(N, S))
