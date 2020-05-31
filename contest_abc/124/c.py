import unittest
from io import StringIO
import sys


def replace_counter(init: int, s: list):
    t = init
    ans = 0

    for c in s:
        if c != t:
            ans += 1
        t ^= 1
    return ans


def resolve():
    S = list(map(int, input()))

    ans = min(replace_counter(0, S), replace_counter(1, S))
    print(ans)


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
        input = """000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10010010"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
