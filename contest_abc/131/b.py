import unittest
from io import StringIO
import sys


def resolve():
    N, L = map(int, input().split())
    tastes = [i + L - 1 for i in range(1, N + 1)]

    tastes.sort(key=lambda x: abs(x))

    print(sum(tastes[1:]))


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
        input = """5 2"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 -1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30 -50"""
        output = """-1044"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
