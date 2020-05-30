import unittest
from io import StringIO
import sys


def resolve():
    S = list(input())

    front = int(''.join(S[:2]))
    back = int(''.join(S[2:]))

    if (1 <= front <= 12 and 1 <= back <= 12):
        print('AMBIGUOUS')
        return

    if (1 <= back <= 12):
        print('YYMM')
        return

    if (1 <= front <= 12):
        print('MMYY')
        return

    print('NA')


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
        input = """1905"""
        output = """YYMM"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0112"""
        output = """AMBIGUOUS"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1700"""
        output = """NA"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
