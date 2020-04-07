import math

a, b, x = map(int, input().split())
s = x / a

if s <= a * b / 2:
    rad = math.atan(b / (2 * s / b))
else:
    rad = math.atan(2 * (a * b - s) / a**2)

print(rad * 180 / math.pi)
