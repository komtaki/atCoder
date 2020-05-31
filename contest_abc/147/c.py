import unittest
from io import StringIO
import sys


def create_input(N):
    honest_comments = []
    for _ in range(N):
        A = int(input())
        comment = []
        for _ in range(A):
            x, y = map(int, input().split())
            x = x - 1
            comment.append((x, y))
        honest_comments.append((A, comment))

    return honest_comments


def resolve():
    N = int(input())
    honest_comments = create_input(N)

    ans = 0
    for n in range(2 ** N):
        tmp_honest = [0] * N
        for i in range(N):
            if n & (1 << i) != 0:
                tmp_honest[i] = 1
        c = tmp_honest.count(1)
        if c <= ans:
            continue
        ok = True
        for i in range(N):
            s = tmp_honest[i]
            A, comment = honest_comments[i]
            for x, y in comment:
                if s == 1 and tmp_honest[x] != y:
                    ok = False
                    break
        if ok:
            ans = max(ans, c)
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
        input = """3
1
2 1
1
1 1
1
2 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1
2 0
1
1 0"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
