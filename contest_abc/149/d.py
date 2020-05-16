

import unittest
from io import StringIO
import sys


def resolve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    point = {"r": P, "s": R, "p": S}
    T = input()

    res = [0] * N
    for i, t in enumerate(T):
        if i - K < 0:
            res[i] = point[t]
        if i - K >= 0 and (res[i - K] == 0 or T[i - K] != T[i]):
            res[i] = point[t]

    print(sum(res))


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
        input = """5 2
8 7 6
rsrpr"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 1
100 10 1
ssssppr"""
        output = """211"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr"""
        output = """4996"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
