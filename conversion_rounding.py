def round_ans(val):
    """
    Rounds currency to the nearest cent
    :param val: Number to be rounded
    :return: Number rounded to the nearest cent
    """
    # shift to cents, round up, and shift back
    var_rounded = (val * 100 * 2 + 1) // 2 / 100
    return "{:.2f}".format(var_rounded)


def to_nzd(to_convert):
    """
    Converts from AUD to NZD
    :param to_convert: Currency to be converted in AUD
    :return: Converted Currency in NZD
    """
    answer = to_convert * 1.21
    return round_ans(answer)


def to_aud(to_convert):
    """
     Converts from NZD to AUd
    ":param to_convert: Currency to be converted in NZD
     :return: Converted temperature in AUD
     """
    answer = to_convert * 0.82

    return round_ans(answer)
