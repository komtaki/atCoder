from math import gcd
import unittest
from io import StringIO
import sys


def resolve():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            a = gcd(i, j)
            for k in range(1, n + 1):
                ans += gcd(a, k)

    print(ans)


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
        input = """2"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """200"""
        output = """10813692"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
