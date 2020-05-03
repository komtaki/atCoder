def resolve():
    n, m = map(int, input().split())
    hhh = list(map(int, input().split()))
    nice = [1] * n

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        ha = hhh[a]
        hb = hhh[b]
        if ha <= hb:
            nice[a] = False
        if ha >= hb:
            nice[b] = False

    print(sum(nice))


# resolve()



import sys
from io import StringIO
import unittest

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
        input = """4 3
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()