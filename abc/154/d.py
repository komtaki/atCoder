import unittest
from io import StringIO
import sys


def resolve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    ans = [0] * N
    max_tmp = [0] * K
    start_index = 0
    for i in range(N - K + 1):
        tmp = P[i: i + K]
        ans[i] = sum(list(range(1, P[i] + 1))) / P[i]
        if sum(max_tmp) < sum(tmp):
            max_tmp = tmp
            start_index = i

    for i in range(N - K, N):
        ans[i] = sum(list(range(1, P[i] + 1))) / P[i]

    print(sum(ans[start_index: start_index + K]))


resolve()


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
        input = """5 3
1 2 2 4 5"""
        output = """7.000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 1
6 6 6 6"""
        output = """3.500000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 4
17 13 13 12 15 20 10 13 17 11"""
        output = """32.000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
