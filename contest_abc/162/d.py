import sys
from io import StringIO
import unittest
from collections import Counter


def resolve():
    n = int(input())
    s = input()
    cnt = Counter(s)
    ans = cnt['R'] * cnt['G'] * cnt['B']

    for i in range(n - 1):
        for j in range(i + 1, n):
            ken = j * 2 - i
            if (ken >= n):
                continue
            if (s[i] != s[j] and s[j] != s[ken] and s[i] != s[ken]):
                ans -= 1

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
RRGB"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB"""
        output = """1800"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
