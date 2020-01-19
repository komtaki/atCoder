import fractions


def lcm(A):
    """N個の最小公倍数

    Args:
        A (list[int])

    Returns:
        int: 最小公倍数
    """
    ans = A[0]
    for i in range(1, len(A)):
        ans = ans * A[i] // fractions.gcd(ans, A[i])
    return ans


def gcd(A):
    """N個の最大公約数

    Args:
        A (list[int])

    Returns:
        int: 最大公約数
    """
    ans = A[0]
    for i in range(1, len(A)):
        ans = fractions.gcd(ans, A[i])
    return ans
