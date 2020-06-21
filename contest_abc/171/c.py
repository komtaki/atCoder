import unittest
from io import StringIO
import sys
import string


def resolve():
    N = int(input())

    alphabets = string.ascii_lowercase
    base_number = 26

    ans = ''
    while N > 0:
        N -= 1
        ans += alphabets[N % base_number]
        N = N // base_number

    print(ans[::-1])


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
        output = """b"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """27"""
        output = """aa"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123456789"""
        output = """jjddja"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """475253"""
        output = """zzzy"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
