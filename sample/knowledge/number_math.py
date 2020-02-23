import math


def get_data_size(data):
    """桁数を求める

    Args:
        data (int): 数値

    Returns:
        [int]: 桁数

    Examples:
        >>> get_data_size(12541)
        5
    """
    return int(math.log10(data) + 1)


def base_10_to_n(X, n):
    """10進数をn進数に変換する

    Args:
        X (int): 10進数の値
        n (int): n進数のn

    Returns:
        str: 10進数をn進数に変換した値

    Examples:
        >>> base_10_to_n(12541, 2)
        '11000011111101'
    """
    X_dumy = X
    out = ''
    while X_dumy > 0:
        out = str(X_dumy % n) + out
        X_dumy = int(X_dumy / n)
    return out


if __name__ == '__main__':
    import doctest
    doctest.testmod()
