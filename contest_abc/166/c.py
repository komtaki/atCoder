def resolve():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))

    A = [[] for _ in range(N)]
    for i in range(M):
        pp, ss = map(int, input().split())
        ss -= 1
        pp -= 1
        A[pp].append(H[ss])
        A[ss].append(H[pp])

    ans = 0
    for j in range(N):
        now = H[j]
        if not A[j] or now > max(A[j]):
            ans += 1

    print(ans)


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