import unittest
from io import StringIO
import sys


def resolve():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = 0
    for value, cost in zip(V, C):
        if value - cost > 0:
            ans += value - cost
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
        input = """3
10 2 5
6 3 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
13 21 6 19
11 30 6 15"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1
50"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
