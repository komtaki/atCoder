import unittest
from io import StringIO
import sys


def resolve():
    A = []
    for i in range(3):
        aa = map(int, input().split())
        A.append(list(aa))

    N = int(input())
    B = []
    for i in range(N):
        B.append(
            int(input())
        )

    ans = 'No'
    flg = 1000

    for bbb in list(B):
        for i in range(3):
            for j in range(3):
                if A[i][j] == bbb:
                    A[i][j] = flg

    for i in range(3):
        if A[i][0] == flg and A[i][1] == flg and A[i][2] == flg:
            ans = 'Yes'
        if A[0][i] == flg and A[1][i] == flg and A[2][i] == flg:
            ans = 'Yes'

    if A[0][0] == flg and A[1][1] == flg and A[2][2] == flg:
        ans = 'Yes'
    if A[0][2] == flg and A[1][1] == flg and A[2][0] == flg:
        ans = 'Yes'

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
        input = """84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """41 7 46
26 89 2
78 92 8
5
6
45
16
57
17"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
