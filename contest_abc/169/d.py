import unittest
from io import StringIO
import sys
import itertools


def factorize(n):
    """素因数分解を行う

    Args:
        n (int): 素因数分解したい数

    Returns:
        fct (list[int]): 素因数分解した結果

    Examples:
        >>> factorize(1000)
        [2, 2, 2, 5, 5, 5]
    """
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct


def resolve():
    N = int(input())

    ans = 0
    factorize_N = factorize(N)

    if not factorize_N:
        print(0)
        return

    for key, value in itertools.groupby(factorize_N):
        count = len(list(value))
        for i in range(1, count + 1):
            count -= i
            if (count < 0):
                break
            ans += 1

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
        input = """24"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """64"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1000000007"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """997764507000"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
