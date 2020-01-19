import string


def create_ascii_letters_list():
    """アルファベット大文字小文字配列作成
    sample: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

    Returns:
        list[str]: アルファベット大文字小文字
    """
    return list((string.ascii_letters))


def create_ascii_lowercase_list():
    """アルファベット小文字配列作成
    sample: abcdefghijklmnopqrstuvwxyz

    Returns:
        list[str]: アルファベット小文字
    """
    return list((string.ascii_lowercase))


def create_ascii_uppercase_list():
    """アルファベット小文字配列作成
    sample: ABCDEFGHIJKLMNOPQRSTUVWXYZ

    Returns:
        list[str]: アルファベット大文字
    """
    return list((string.ascii_uppercase))
