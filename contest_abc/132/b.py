import unittest
from io import StringIO
import sys


def resolve():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0

    for i in range(1, N - 1):
        tmp = sorted(P[i - 1:i + 2])

        if tmp[1] == P[i]:
            ans += 1

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
        input = """5
1 3 5 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
9 6 3 2 5 8 7 4 1"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
