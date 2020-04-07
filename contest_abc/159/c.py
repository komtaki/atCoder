# import itertools
# import math

import unittest
from io import StringIO
import sys

from decimal import Decimal, getcontext

getcontext().prec = 99


def resolve():
    L = int(input())

    ans = Decimal(L / 3) ** 3

    print(ans)


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
        input = """3"""
        output = """1.000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """999"""
        output = """36926037.000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
