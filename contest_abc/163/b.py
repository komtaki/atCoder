import unittest
from io import StringIO
import sys


def resolve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    if (N < sum(A)):
        print(-1)
        return

    print(N - sum(A))


# resolve()


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
        input = """41 2
5 6"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2
5 6"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 2
5 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """314 15
9 26 5 35 8 9 79 3 23 8 46 2 6 43 3"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
