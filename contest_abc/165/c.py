import unittest
from io import StringIO
import sys
import itertools


def resolve():
    N, M, Q = map(int, input().split())
    a = [0 for i in range(Q)]
    b = [0 for i in range(Q)]
    c = [0 for i in range(Q)]
    d = [0 for i in range(Q)]

    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
        b[i] -= 1
        a[i] -= 1
    ans = 0

    for seq in itertools.combinations_with_replacement(range(M), N):
        tmp = 0
        for i in range(Q):
            if seq[b[i]] - seq[a[i]] == c[i]:
                tmp += d[i]
        ans = max(ans, tmp)

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
        input = """3 4 3
1 3 3 100
1 2 2 10
2 3 2 10"""
        output = """110"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 6 10
2 4 1 86568
1 4 0 90629
2 3 0 90310
3 4 1 29211
3 4 3 78537
3 4 2 8580
1 2 1 96263
1 4 2 2156
1 2 0 94325
1 4 3 94328"""
        output = """357500"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 1
1 10 9 1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
