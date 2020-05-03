from io import StringIO
import sys
import unittest
from collections import defaultdict


def resolve():
    s = input()

    cnt = defaultdict(int)
    cnt[0] += 1
    tmp = 0
    for i, c in enumerate(s[::-1]):
        c = int(c)
        tmp = (tmp + c * pow(10, i, 2019)) % 2019
        cnt[tmp] += 1

    ans = sum(c * (c - 1) // 2 for c in cnt.values())
    print(ans)


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
        input = """1817181712114"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14282668646"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2119"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
