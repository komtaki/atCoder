import fractions


def lcm(N: int, A: list) -> int:
    """N個の最小公倍数

    Args:
        N (int): [description]
        A (list): [description]

    Returns:
        int: 最小公倍数
    """
    ans = A[0]
    for i in range(1, N):
        ans = ans * A[i] // fractions.gcd(ans, A[i])
    return ans


def gcd(N: int, A: list) -> int:
    """N個の最大公約数

    Args:
        N (int): [description]
        A (list): [description]

    Returns:
        int: 最大公約数
    """
    ans = A[0]
    for i in range(1, N):
        ans = fractions.gcd(ans, A[i])
    return ans
