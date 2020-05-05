import unittest
from io import StringIO
import sys


def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy > 0:
        out = str(X_dumy % n) + out
        X_dumy = int(X_dumy / n)
    return out


def resolve():
    N, K = map(int, input().split())

    ans = Base_10_to_n(N, K)
    ans_list = list(str(ans))

    print(len(ans_list))


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
        input = """11 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1010101 10"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265 3"""
        output = """18"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
