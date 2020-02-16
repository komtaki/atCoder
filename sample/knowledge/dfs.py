from collections import deque


# abc 151
def dfs(field, s):
    MOVE = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([(0, s)])
    dist = [[-1] * w for _ in range(h)]

    d, i, j = -1, -1, -1
    while q:
        d, (i, j) = q.popleft()
        if dist[i][j] != -1:
            continue
        dist[i][j] = d
        for di, dj in MOVE:
            ni, nj = i + di, j + dj
            if not 0 <= ni < h or not 0 <= nj < w:
                continue
            if field[ni][nj] == '#':
                continue
            if dist[ni][nj] != -1:
                continue
            q.append((d + 1, (ni, nj)))
    return d, i, j


h, w = map(int, input().split())
field = [input() for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if field[i][j] == '.':
            d, i, j = dfs(field, (i, j))
            ans = max(ans, d)
print(ans)
