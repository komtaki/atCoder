import sys
from io import StringIO
import unittest
import math


def resolve():
    n = int(input())
    values = list(map(int, input().split(' ')))

    values.sort(reverse=True)
    ans = 0

    for i in range(1, n):
        ans += values[math.floor(i / 2)]
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
        input = """4
2 2 1 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
1 1 1 1 1 1 1"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
2 2 1 3 3"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
