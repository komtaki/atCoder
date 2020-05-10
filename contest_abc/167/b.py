import unittest
from io import StringIO
import sys


def resolve():
    A, B, C, K = map(int, input().split())

    if A >= K:
        ans = K
    else:
        ans = A + (K - A) * 0 + (K - A - B) * -1

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
        input = """2 1 1 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2000000000 0 0 2000000000"""
        output = """2000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
