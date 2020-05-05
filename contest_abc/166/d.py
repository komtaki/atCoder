def resolve():
    N = int(input())
    facts = [i ** 5 for i in range(120)]
    for a, a5 in enumerate(facts):
        for b, b5 in enumerate(facts):
            if a5 + b5 == N:
                print(a, -b)
                break
            if a5 - b5 == N:
                print(a, b)
                break
        else:
            continue
        break


resolve()


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
        input = """33"""
        output = """2 -1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1"""
        output = """0 -1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()