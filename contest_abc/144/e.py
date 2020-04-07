import heapq
import numpy

N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))


def solve(member, max_try):
    sorted_f = numpy.array(sorted(F))
    sorted_a = numpy.array(sorted(A, reverse=1))

    a_a = sorted_f * sorted_a

    aa = [[-x, x] for x in a_a]

    heapq.heapify(aa)

    for i in range(K):
        x, y = heapq.heappop(aa)
        tmp = sorted_f / (sorted_a - 1)
        heapq.heappush(aa, [- tmp, tmp - 1])

    aaa = [x[1] for x in aa]

    return max(aaa)


print(solve(N, K))
