# import itertools
# import math


import unittest
from io import StringIO
import sys


def resolve():
    # N = int(input())
    # S = input()
    N, R = map(int, input().split())
    # A = list(map(int, input().split()))

    # P = []
    # S = []
    # for i in range(N):
    #     pp, ss = map(int, input().split())
    #     P.append(pp)
    #     S.append(ss)

    if N < 10:
        ans = R + (100 * (10 - N))
        print(ans)
        return

    print(R)


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
        input = """2 2919"""
        output = """3719"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """22 3051"""
        output = """3051"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
