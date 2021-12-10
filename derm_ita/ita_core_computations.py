import math
import numpy as np
from PIL import Image
import skimage
from patchify import patchify

from boarder_removal import get_border_removal_size


def compute_ita_from_lab(lab):
    """
    This function computes the ITA value of the image along with ignore any pixels that are completely black
    """
    # get the luminance and b values wihtin +- 1 std from mean
    l = lab[:, :, 0]
    l = np.where(l != 0, l, np.nan)
    std = np.nanstd(l)
    mean = np.nanmean(l)

    l = np.where(l >= mean - std, l, np.nan)
    l = np.where(l <= mean + std, l, np.nan)

    b = lab[:, :, 2]
    std = np.nanstd(b)
    mean = np.nanmean(b)
    b = np.where(b >= mean - std, b, np.nan)
    b = np.where(b <= mean + std, b, np.nan)

    ita = math.atan2(np.nanmean(l) - 50, np.nanmean(b)) * (180 / np.pi)
    return ita


def compute_ita(image: Image):
    """
    This function takes in an image and outputs the ITA value of image. To compute the ITA value the image needs
    to be converted from an RGB format to a LAB format type.
    :param image: input image
    """

    lab = np.array(skimage.color.rgb2lab(image))

    return compute_ita_from_lab(lab)


def format_image_and_get_lab_patches(image: Image, border_removal_percentage: float = 0.04, patch_width: int = 8):
    """
    This function will remove the boarder, convert the whole image from RGB to LAB and then using Patchify
    tool it will create patches. These patches are non-overlapping that create a grid over the whole image.
    :param image: input image
    :param border_removal_percentage: how much of the boarder to remove
    :param patch_width: the width size of the patches in pixels.
    :return: A list of patches that are in a LAB format
    """

    # Crop image to remove the pixels from the boarder
    w, h = image.size
    removal_size = get_border_removal_size(image, border_removal_percentage, patch_width)
    cropped_area = (removal_size, removal_size, w - removal_size, h - removal_size)
    cropped_image = image.crop(cropped_area)

    # Convert image to lab values
    lab = np.array(skimage.color.rgb2lab(cropped_image))

    # Get the patches
    return patchify(lab, (patch_width, patch_width, 3), step=patch_width)


def compute_ita_from_lab(lab_image):
    """
    This function computes the ITA value of the image along with ignore any pixels that are completely black
    :param lab_image:  input image formatted in LAB color space
    :return: the ITA value from the input image
    """
    # get the luminance and b values wihtin +- 1 std from mean
    l = lab_image[:, :, 0]
    l = np.where(l != 0, l, np.nan)
    std = np.nanstd(l)
    mean = np.nanmean(l)

    l = np.where(l >= mean - std, l, np.nan)
    l = np.where(l <= mean + std, l, np.nan)

    b = lab_image[:, :, 2]
    std = np.nanstd(b)
    mean = np.nanmean(b)
    b = np.where(b >= mean - std, b, np.nan)
    b = np.where(b <= mean + std, b, np.nan)

    ita = math.atan2(np.nanmean(l) - 50, np.nanmean(b)) * (180 / np.pi)
    return ita


def compute_ita(image: Image, crop_border=False, border_removal_percentage: float = 0.04, patch_width: int = 8):
    """
    This function takes in an image and outputs the ITA value of image. To compute the ITA value the image needs
    to be converted from an RGB format to a LAB format type.

    :param image: input image
    :param crop_border: option to remote part of the baorder
    :param border_removal_percentage: how much of the boarder to remove
    :param patch_width: the width size of the patches in pixels.
    :return: ITA value computed from the input image
    """

    if crop_border:
        w, h = image.size
        removal_size = get_border_removal_size(image, border_removal_percentage, patch_width)
        cropped_area = (removal_size, removal_size, w - removal_size, h - removal_size)
        image = image.crop(cropped_area)

    lab = np.array(skimage.color.rgb2lab(image))

    return compute_ita_from_lab(lab)
