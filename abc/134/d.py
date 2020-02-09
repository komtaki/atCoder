# import itertools
# import math

import unittest
from io import StringIO
import sys


def resolve():
    input = sys.stdin.readline
    N = int(input())
    # S = input()
    # A, B = map(int, input().split())
    A = list(map(int, input().split()))

    # P = []
    # S = []
    # for i in range(N):
    #     pp, ss = map(int, input().split())
    #     P.append(pp)
    #     S.append(ss)

    isBalls = [0] * (N + 1)
    for k in reversed(range(1, N + 1)):
        num = sum([isBalls[k * i] for i in range(1, N // k + 1)])
        if num % 2 != A[k - 1]:
            isBalls[k] = 1

    M = sum(isBalls)
    ans = [i for i in range(1, N + 1) if isBalls[i] > 0]

    print(M)
    if ans:
        print(' '.join(map(str, ans)))


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
1 0 0"""
        output = """1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
