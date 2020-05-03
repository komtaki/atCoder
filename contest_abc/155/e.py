import unittest
from io import StringIO
import sys


def resolve():
    N = list(map(int, list(input())))
    N.reverse()
    N.append(0)
    res = 0
    for i in range(len(N) - 1):
        n = N[i]
        if n < 5:
            res += n
        else:
            if n == 5:
                if N[i + 1] >= 5:
                    N[i + 1] += 1
            else:
                N[i + 1] += 1
            res += 10 - n

    if N[-1] > 0:
        res += 1

    print(res)


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
        input = """36"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """91"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265358979323846264338327950288419716939937551058209749445923078164062862089986280348253421170"""
        output = """243"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
