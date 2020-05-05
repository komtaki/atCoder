import unittest
from io import StringIO
import sys


def resolve():
    N, M = map(int, input().split())
    ans = 0

    if N > 1:
        ans = N * (N - 1) // 2
    if M > 1:
        ans += M * (M - 1) // 2

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
        input = """2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """13 3"""
        output = """81"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """0 3"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
