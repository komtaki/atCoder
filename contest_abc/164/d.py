def retry(list_S, len_S, ans=0, start_ii=0):
    if len_S <= 3 or start_ii > len_S - 3:
        return ans

    for start_i in range(start_ii, len_S - 3):
        for last_i in range(start_i + 3, len_S):
            tmp = ''.join(list_S[start_i:last_i + 1])

            if (int(tmp) % 2019) == 0:
                ans += 1
                return retry(list_S, len_S, ans, last_i)

    return ans


def resolve():
    S = list(input())
    len_S = len(S)
    print(retry(list_S=S, len_S=len_S))


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
        input = """1817181712114"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """14282668646"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2119"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()