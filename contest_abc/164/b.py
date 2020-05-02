import unittest
from io import StringIO
import sys


def resolve():
    A, B, C, D = map(int, input().split())

    while A > 0 or C > 0:
        C -= B
        if C <= 0:
            print('Yes')
            return
        A -= D
        if A <= 0:
            print('No')
            return


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
        input = """10 9 10 10"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """46 4 40 5"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
