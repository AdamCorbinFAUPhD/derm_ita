from PIL import Image
import math

# boarder trimming
def get_border_removal_size(image: Image, border_removal_percentage: float = .04, patch_width: int = 8):
    """
    This function will compute the border removal size. When computing the boarder removal the patch size becomes
    important the output shape of the image will always be an even factor of the patch size. This allows the later
    computations to evenly fit the image.
    :param image: input image to get the dimentions
    :param border_removal_percentage: how much of the boarder to remove
    :param patch_width: the width size of the patches in pixels.
    :return: how many pixes to be removed around the boarder
    """
    w, h = image.size
    return int(math.ceil(w * border_removal_percentage / patch_width)) * patch_width


def trim_boarder_from_image(pil_image: Image):
    """
    This function will take an image, remove the boarder and return the cropped image.
    :param pil_image: original input image
    :return: the cropped image after the boarder removal
    """
    w, h = pil_image.size
    removal_size = get_border_removal_size(pil_image)
    cropped_area = (removal_size, removal_size, w - removal_size, h - removal_size)
    cropped_image = pil_image.crop(cropped_area)
    return cropped_image
