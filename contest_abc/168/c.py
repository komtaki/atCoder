import unittest
from io import StringIO
import sys
import math


def resolve():
    A, B, H, M = map(int, input().split())

    radian = math.pi * 2 * (H / 12 + (M / 60) / 12 - M / 60)

    cos_AB = math.cos(radian)
    ans = A ** 2 + B ** 2 - 2 * A * B * cos_AB

    print(math.sqrt(ans))


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
        input = """3 4 9 0"""
        output = """5.00000000000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4 10 40"""
        output = """4.56425719433005567605"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
