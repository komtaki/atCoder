import unittest
from io import StringIO
import sys
from math import gcd


def list_lcm(A):
    """N個の最小公倍数
    Args:
        A (list[int])

    Returns:
        int: 最小公倍数

    Examples:
        >>> list_lcm([12, 34, 54, 65])
        119340
    """
    ans = A[0]
    for i in range(1, len(A)):
        ans = ans * A[i] // gcd(ans, A[i])
    return ans


def resolve():
    A, B, C, D = map(int, input().split())
    A -= 1

    lcm_C_D = list_lcm([C, D])
    ans_B = B - B // C - B // D + B // lcm_C_D
    ans_A = A - A // C - A // D + A // lcm_C_D

    print(ans_B - ans_A)


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
        input = """4 9 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 40 6 8"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265358979323 846264338327950288 419716939 937510582"""
        output = """532105071133627368"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
