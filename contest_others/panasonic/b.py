# import itertools
# import math


import unittest
from io import StringIO
import sys


def resolve():
    H, W = map(int, input().split())

    if H == 1 or W == 1:
        print(1)
        return

    count = H * W
    ans = count // 2

    if count % 2 != 0:
        ans += 1

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
        input = """4 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 3"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000 1000000000"""
        output = """500000000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
