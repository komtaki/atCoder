import unittest
from io import StringIO
import sys


def resolve():
    N, M = map(int, input().split())

    req = [list(map(int, input().split())) for i in range(M)]

    for i in range(10000):
        st = str(i)
        if len(st) != N:
            continue

        ok = True
        for s, c in req:
            if int(st[s - 1]) != int(c):
                ok = False
        if ok:
            print(st)
            return

    print(-1)


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
        input = """3 3
1 7
3 2
1 7"""
        output = """702"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
2 1
2 3"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1
1 0"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
    resolve()
