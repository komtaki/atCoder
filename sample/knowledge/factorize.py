def factorize(n):
    """素因数分解を行う

    Args:
        n (int): 素因数分解したい数

    Returns:
        fct (list[int]): 素因数分解した結果

    Examples:
        >>> factorize(1000)
        [2, 2, 2, 5, 5, 5]
    """
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct


if __name__ == '__main__':
    import doctest
    doctest.testmod()
