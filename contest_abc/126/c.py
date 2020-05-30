import unittest
from io import StringIO
import sys


def resolve():
    N, K = map(int, input().split())

    ans = 0
    for i in range(1, N + 1):
        tmp = 1
        while i * tmp < K:
            tmp *= 2
        ans += 1 / tmp
    print(ans / N)


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
        input = """3 10"""
        output = """0.145833333333"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000 5"""
        output = """0.999973749998"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
