import unittest
from io import StringIO
import sys
import bisect


def resolve():
    n = int(input())
    li = list(map(int, input().split()))
    ans = 0

    li.sort()

    for i in range(n):
        for j in range(i + 1, n):
            cnt = bisect.bisect_left(li, li[i] + li[j])

            ans += cnt - j - 1

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
        input = """4
3 4 2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1000 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
218 786 704 233 645 728 389"""
        output = """23"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
