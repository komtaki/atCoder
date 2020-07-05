import sys
from io import StringIO
import unittest


def resolve():
    N = input()

    if N == '10000':
        print(0)
        return

    if int(N) <= 1000:
        print(1000 - int(N))
        return

    if (N[1] == '0' and N[2] == '0' and N[3] == '0'):
        print(0)
        return

    ans = 1000 * (int(N[0]) + 1) - int(N)
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
        input = """1900"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
