import unittest
from io import StringIO
import sys


def resolve():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max_distance = 0

    for i in range(N - 1):
        max_distance = max(max_distance, A[i + 1] - A[i])

    max_distance = max(max_distance, A[0] + K - A[N - 1])
    print(K - max_distance)


resolve()


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[: -1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """20 3
5 10 15"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 3
0 5 15"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
