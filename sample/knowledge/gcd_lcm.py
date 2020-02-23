from fractions import gcd


def list_lcm(A):
    """N個の最小公倍数
    Args:
        A (list[int])

    Returns:
        int: 最小公倍数

    Examples:
        >>> list_lcm([12, 34, 54, 65])
        119340
    """
    ans = A[0]
    for i in range(1, len(A)):
        ans = ans * A[i] // gcd(ans, A[i])
    return ans


def list_gcd(A):
    """N個の最大公約数
    Args:
        A (list[int])

    Returns:
        int: 最大公約数

    Examples:
        >>> list_gcd([1300, 34, 54, 60])
        2
    """
    ans = A[0]
    for i in range(1, len(A)):
        ans = gcd(ans, A[i])
    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()
