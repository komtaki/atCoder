import sys
from io import StringIO
import unittest
from collections import Counter


def resolve():
    n = int(input())
    s = input()
    cnt = Counter(s)
    ans = cnt['R'] * cnt['G'] * cnt['B']

    for i in range(n):
        l = 1
        si = s[i]
        while i + l * 2 < n:
            if si != s[i + l] and si != s[i + l *
                                          2] and s[i + l] != s[i + l * 2]:
                ans -= 1
            l += 1

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
