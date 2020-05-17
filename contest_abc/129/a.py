import unittest
from io import StringIO
import sys
import itertools


def resolve():
    distance = list(map(int, input().split()))

    ans = sum(distance)
    for group in itertools.combinations(distance, 2):
        ans = min(sum(group), ans)

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
        input = """1 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2 3"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
