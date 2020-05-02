

import unittest
from io import StringIO
import sys


def resolve():
    S, W = map(int, input().split())

    if W >= S:
        print('unsafe')
        return

    print('safe')


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
        input = """4 5"""
        output = """unsafe"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 2"""
        output = """safe"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10"""
        output = """unsafe"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
