# import itertools
# import math


import unittest
from io import StringIO
import sys


def resolve():
    X = int(input())

    ans = X // 500 * 1000

    X = X % 500

    ans += X // 5 * 5

    print(ans)


resolve()


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
        input = """1024"""
        output = """2020"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000"""
        output = """2000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
