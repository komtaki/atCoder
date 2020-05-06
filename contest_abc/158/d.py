import unittest
from io import StringIO
import sys


def resolve():
    S = input()
    Q = int(input())

    rev = 0
    append_front_rev = ''
    append_rear = ''

    for i in range(Q):
        T = input().split()

        if (T[0] == "1"):
            rev ^= 1
            continue

        if (T[0] == "2" and T[1] == "1"):
            if rev == 0:
                append_front_rev += T[2]
            else:
                append_rear += T[2]
            continue

        if (T[0] == "2" and T[1] == "2"):
            if rev == 0:
                append_rear += T[2]
            else:
                append_front_rev += T[2]
            continue

    ans = append_front_rev[::-1] + S + append_rear
    if rev:
        ans = ans[::-1]

    print("".join(ans))


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
        input = """a
4
2 1 p
1
2 2 c
1"""
        output = """cpa"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """a
6
2 2 a
2 1 b
1
2 2 c
1
1"""
        output = """aabc"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """y
1
2 1 x"""
        output = """xy"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
