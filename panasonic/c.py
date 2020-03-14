from decimal import Decimal, getcontext

import unittest
from io import StringIO
import sys

getcontext().prec = 99


def resolve():
    A, B, C = map(int, input().split())

    ab = Decimal(A).sqrt() + Decimal(B).sqrt()
    c = Decimal(C).sqrt()
    ans = 'Yes' if ab < c else 'No'
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
        input = """2 3 9"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 10"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
