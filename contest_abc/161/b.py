import unittest
from io import StringIO
import sys


def resolve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    if M > len(A):
        print('No')
        return

    A.sort(reverse=True)
    total = sum(A)

    for i in range(M):
        if (A[i] < total * (1 / (4 * M))):
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
        input = """4 1
5 4 2 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
380 19 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12 3
4 56 78 901 2 345 67 890 123 45 6 789"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
