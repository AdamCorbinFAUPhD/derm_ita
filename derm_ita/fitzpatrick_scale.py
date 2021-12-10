def get_fitzpatrick_type(ita):
    """
    This function will take a ita value and return the Fitzpatrick skin tone scale
    :param ita:
    :return:
    """
    if ita <= 10:
        return "6"
    elif 10 < ita <= 19:
        return "5"
    elif 19 < ita <= 28:
        return "4"
    elif 28 < ita <= 41:
        return "3"
    elif 41 < ita <= 55:
        return "2"
    elif 55 < ita:
        return "1"
    else:
        print(f"None cat: {ita}")


def get_fitzpatrick2_type(ita):
    """
    This function will take a ita value and return the Fitzpatrick skin tone scale
    https://arxiv.org/pdf/2104.14685.pdf
    :param ita:
    :return:
    """
    if ita < -50:
        return "6"
    elif -50 <= ita < -25:
        return "5"
    elif -25 <= ita < 0:
        return "4"
    elif 0 <= ita < 25:
        return "3"
    elif 25 <= ita < 50:
        return "2"
    elif 50 <= ita:
        return "1"
    else:
        print(f"None cat: {ita}")


def add_groh_ita_category(ita):
    if ita <= -25:
        return "Type6"
    elif -25 < ita <= 0:
        return "Type5"
    elif 0 < ita <= 12:
        return "Type4"
    elif 12 < ita <= 23:
        return "Type3"
    elif 23 < ita <= 40:
        return "Type2"
    elif 40 < ita:
        return "Type1"