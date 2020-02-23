import numpy as np


def dp(h, n, aaa, bbb):
    """動的計画法

    Args:
        h (int): [description]
        n (int): [description]
        aaa (list[int]): [description]
        bbb (list[int]): [description]

    Returns:
        int:

    Examples:
        >>> dp(9, 3, [8, 4, 2], [3, 2, 1])
        4

    Note:
        https://atcoder.jp/contests/abc153/tasks/abc153_e
    """
    aaa = np.array(aaa)
    bbb = np.array(bbb)

    dp = np.zeros(h + 1, dtype=np.int64)
    for i in range(1, h + 1):
        dp[i] = (dp[i - aaa] + bbb).min()
    return dp[h]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
