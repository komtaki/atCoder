# import itertools
# import math


def clear_maze(sx, sy, gx, gy, maze):

    INF = 100000000

    field_y_length = len(maze)
    field_x_length = len(maze[0])
    distance = [[INF] * field_x_length] * field_y_length

    def bfs():
        queue = []

        queue.insert(0, (sy, sx))

        distance[sy][sx] = 0

        while len(queue):
            y, x = queue.pop()

            if x == gx and y == gy:
                break

            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

                if (0 <= nx and nx < field_x_length and 0 <= ny and ny <
                        field_y_length and maze[ny][nx] != '#' and distance[ny][nx] == INF):
                    queue.insert(0, (ny, nx))
                    distance[ny][nx] = distance[y][x] + 1

        return distance[gy][gx]

    return bfs()


def solve(H, W, S):
    ans = 0
    for shh in range(H):
        for sww in range(W):
            for ghh in range(H):
                for gww in range(W):
                    if shh != ghh and sww != gww and S[shh][sww] != '#' and S[ghh][gww] != '#':
                        tmp = clear_maze(sww, shh, gww, ghh, S)
                        ans = max(ans, tmp)
    return ans


# N = int(input())
# S = input()
H, W = map(int, input().split())

S = ['#'] * H
for i in range(H):
    S[i] = list(input())

print(solve(H, W, S))
