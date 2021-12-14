def get_kinyanjui_type(ita):
    """
    This function will take a ita value and return the Fitzpatrick skin tone scale
    https://arxiv.org/pdf/1910.13268.pdf
    :param ita:
    :return:
    """
    if ita <= 10:
        return "dark"
    elif 10 < ita <= 19:
        return "tan1"
    elif 19 < ita <= 28:
        return "tan2"
    elif 28 < ita <= 34.5:
        return "int1"
    elif 34.5 < ita <= 41:
        return "int2"
    elif 41 < ita <= 48:
        return "lt1"
    elif 48 < ita <= 55:
        return "lt2"
    elif 55 < ita:
        return "very_lt"
    else:
        print(f"None cat: {ita}")


def get_kinyanjui_groh_type(ita):
    """
    This function will take a ita value and return the Fitzpatrick skin tone scale
    https://openaccess.thecvf.com/content/CVPR2021W/ISIC/papers/Groh_Evaluating_Deep_Neural_Networks_Trained_on_Clinical_Images_in_Dermatology_CVPRW_2021_paper.pdf
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


def get_del_bino_type(ita):
    """
    This function will take a ita value and return the Fitzpatrick skin tone scale
    https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0241843&type=printable
    :param ita:
    :return:
    """
    if ita < -30:
        return "dark"
    elif -30 < ita <= 10:
        return "brown"
    elif 10 < ita <= 28:
        return "tan"
    elif 28 < ita <= 41:
        return "intermediate"
    elif 41 < ita <= 55:
        return "light"
    elif 55 < ita:
        return "very light"
    else:
        print(f"None cat: {ita}")


def get_fitzpatrick_type(ita):
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


def get_groh_ita_category(ita):
    """
    Developed based on the empirical distribution of ITA scores minimizing overall error
    https://openaccess.thecvf.com/content/CVPR2021W/ISIC/papers/Groh_Evaluating_Deep_Neural_Networks_Trained_on_Clinical_Images_in_Dermatology_CVPRW_2021_paper.pdf
    :param ita:
    :return:
    """
    if ita <= -25:
        return "6"
    elif -25 < ita <= 0:
        return "5"
    elif 0 < ita <= 12:
        return "4"
    elif 12 < ita <= 23:
        return "3"
    elif 23 < ita <= 40:
        return "2"
    elif 40 < ita:
        return "1"