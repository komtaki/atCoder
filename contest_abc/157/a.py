import unittest
from io import StringIO
import sys


def resolve():
    N = int(input())

    if N % 2 == 0:
        print(N // 2)
        return

    ans = N // 2
    print(ans + 1)


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
        input = """5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100"""
        output = """50"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
