import unittest
from io import StringIO
import sys


def resolve():
    N, M = map(int, input().split())

    shops = []
    for i in range(N):
        aa, bb = map(int, input().split())
        shops.append([aa, bb])

    shops.sort(key=lambda x: x[0])

    rem = M
    ans = 0
    for shop in shops:
        buy = min(rem, shop[1])
        ans += buy * shop[0]
        rem -= buy

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
        input = """2 5
4 9
2 4"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 30
6 18
2 5
3 10
7 9"""
        output = """130"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 100000
1000000000 100000"""
        output = """100000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
