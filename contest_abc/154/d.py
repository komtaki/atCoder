import unittest
from io import StringIO
import sys
import itertools


def resolve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    P = [(1 + p) / 2 for p in P]
    accumulate_P = [0] + list(itertools.accumulate(P))

    ans = 0
    for ii in range(N - K + 1):
        range_sum_P = accumulate_P[ii + K] - accumulate_P[ii]
        ans = max(ans, range_sum_P)

    print(ans)


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
        input = """3 3
700 384 43"""
        output = """565"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 1
6 6 6 6"""
        output = """3.5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 4
17 13 13 12 15 20 10 13 17 11"""
        output = """32.0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
