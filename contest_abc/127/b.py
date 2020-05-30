import unittest
from io import StringIO
import sys


def resolve():
    r, D, x = map(int, input().split())

    ans = [0 for _ in range(11)]
    ans[0] = x
    for i in range(1, 11):
        ans[i] = r * ans[i - 1] - D

    print('\n'.join(map(str, ans[1:])))


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
        input = """2 10 20"""
        output = """30
50
90
170
330
650
1290
2570
5130
10250"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 40 60"""
        output = """200
760
3000
11960
47800
191160
764600
3058360
12233400
48933560"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
