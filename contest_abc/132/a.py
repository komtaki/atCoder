import unittest
from io import StringIO
import sys
import collections


def resolve():
    S = list(input())

    counter_S = collections.Counter(S)

    if len(counter_S) != 2:
        print("No")
        return

    for value in counter_S.values():
        if value != 2:
            print("No")
            return

    print("Yes")


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
        input = """ASSA"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """STOP"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """FFEE"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """FREE"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
