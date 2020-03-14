import sys
from io import StringIO
import unittest


def resolve():
    S = input()
    c = list(S)
    count = len(c)
    if count == 1 or count % 2 != 0:
        print('No')
        return

    if count == 2 and S != 'hi':
        print('No')
        return

    for i in range(0, count - 2, 2):
        if ''.join(c[i:i + 2]) != 'hi':
            print('No')
            return
    print('Yes')


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
        input = """hihi"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """hi"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """ha"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
