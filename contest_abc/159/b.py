import unittest
from io import StringIO
import sys


def ispalindrome(str): return 1 if str == str[::-1] else 0


def resolve():
    S = list(input())

    if not ispalindrome(''.join(S)):
        print('No')
        return

    num = len(S)
    half = num // 2

    half_1 = S[0:half]
    half_2 = S[half + 1:]

    if not ispalindrome(''.join(half_1)):
        print('No')
        return

    if not ispalindrome(''.join(half_2)):
        print('No')
        return

    print('Yes')





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
        input = """akasaka"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """level"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """atcoder"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
