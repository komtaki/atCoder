import string


def create_ascii_letters_list():
    """アルファベット大文字小文字配列作成

    Returns:
        list[str]: アルファベット大文字小文字

    Examples:
        >>> create_ascii_letters_list()
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    """
    return list((string.ascii_letters))


def create_ascii_lowercase_list():
    """アルファベット小文字配列作成

    Returns:
        list[str]: アルファベット小文字

    Examples:
        >>> create_ascii_lowercase_list()
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    """
    return list((string.ascii_lowercase))


def create_ascii_uppercase_list():
    """アルファベット小文字配列作成

    Returns:
        list[str]: アルファベット大文字

    Examples:
        >>> create_ascii_lowercase_list()
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    """
    return list((string.ascii_uppercase))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
