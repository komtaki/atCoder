import math


def get_data_size(data):
    """桁数を求める

    Args:
        data (int): 数値

    Returns:
        [int]: 桁数
    """
    return int(math.log10(data) + 1)
