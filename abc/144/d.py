from numpy import arctan, pi

a, b, x = list(map(int, input().split()))

if x > 0.5 * a * a * b:
    print(arctan(2 / a * (b - x / (a * a))) / (pi) * 180)
else:
    print(arctan(a * b * b / (2 * x)) / (pi) * 180)
