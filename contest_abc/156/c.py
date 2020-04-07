# import itertools
# import math


import unittest
from io import StringIO
import sys


def resolve():
    N = int(input())
    X = list(map(int, input().split()))

    ans = 100000000000

    for p in range(1, 101):
        tmp = 0
        for x in X:
            tmp = tmp + ((x - p) ** 2)

        ans = min(tmp, ans)

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
        input = """2
1 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
14 14 2 13 56 2 37"""
        output = """2354"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
