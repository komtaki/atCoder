# import itertools
# import math


import unittest
from io import StringIO
import sys


def resolve():
    N = list(input())

    for nn in N:
        if (nn == str(7)):
            print("Yes")
            return

    print("No")


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
        input = """117"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """777"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
