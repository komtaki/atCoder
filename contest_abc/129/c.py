import unittest
from io import StringIO
import sys


MOD = 10 ** 9 + 7


def resolve():
    N, M = map(int, input().split())

    broken = [False] * (N + 1)
    dp = [0 for _ in range(N + 1)]
    dp[0] = 1

    for _ in range(M):
        broken[int(input())] = True

    for i in range(1, N + 1):
        if broken[i]:
            continue

        if i == 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= MOD

    print(dp[N])


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """6 1
3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2
4
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 5
1
23
45
67
89"""
        output = """608200469"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
