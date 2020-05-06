import unittest
from io import StringIO
import sys
import math


def resolve():
    A, B = map(int, input().split())

    for i in range(10000):
        tmp_8 = math.floor(i * 0.08)
        tmp_10 = math.floor(i * 0.1)

        if (tmp_8 > 0 and tmp_10 > 0 and tmp_8 == A and tmp_10 == B):
            print(i)
            return

    print(-1)


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
        input = """2 2"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 10"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """19 99"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
