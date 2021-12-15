from PIL import Image
import os
from os.path import dirname, abspath
import derm_ita


def test_whole_image():
    baseDir = dirname(abspath(__file__)) + os.path.sep
    whole_image_ita = derm_ita.get_ita(Image.open(baseDir +"/000b6317b3be6d504e212a50e4d5667f.jpg"))
    assert whole_image_ita == 63.17057942677103


def test_kinyanjui_type():
    baseDir = dirname(abspath(__file__)) + os.path.sep
    whole_image_ita = derm_ita.get_ita(Image.open(baseDir + "/000b6317b3be6d504e212a50e4d5667f.jpg"))
    kinyanjui_type = derm_ita.get_kinyanjui_type(whole_image_ita)
    assert kinyanjui_type == "very_lt"