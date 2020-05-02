import unittest
from io import StringIO
import sys


def resolve():
    K = int(input())
    A, B = map(int, input().split())

    for i in range(A, B + 1):
        if (i % K) == 0:
            print('OK')
            return

    print('NG')


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
        input = """7
500 600"""
        output = """OK"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 7"""
        output = """NG"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
11 11"""
        output = """OK"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
