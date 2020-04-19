import unittest
from io import StringIO
import sys
import collections


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = collections.Counter(A)

    for i in range(1, N + 1):
        print(ans[i])


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
        input = """5
1 1 2 2"""
        output = """2
2
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
1 1 1 1 1 1 1 1 1"""
        output = """9
0
0
0
0
0
0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
1 2 3 4 5 6"""
        output = """1
1
1
1
1
1
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
