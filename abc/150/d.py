import fractions

N, M = map(int, input().split())
A = list(map(int, input().split()))

A = list(set(A))

gcd = A[0]
for i in range(1, len(A)):
    gcd = gcd * A[i] // fractions.gcd(gcd, A[i])

half_gcd = gcd // 2

count = (M + half_gcd) // gcd

print(count)
