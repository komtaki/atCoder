import sys
from io import StringIO
import unittest


def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    loop = [1]
    arrived = [False] * N
    now = 1
    arrived[now - 1] = True

    for i in range(K):
        now = A[now - 1]
        if not arrived[now - 1]:
            arrived[now - 1] = True
            loop.append(now)
        else:
            loop = loop[loop.index(now):]
            arrive = loop[(K - (i + 1)) % len(loop)]
            print(arrive)
            return

    print(now)


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
        input = """4 5
3 2 4 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 727202214173249351
6 5 2 5 3 2"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
