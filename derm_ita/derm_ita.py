# Different approaches
import math

import numpy as np
import skimage
from PIL import Image

from cropped_center import get_cropped_center_patches_ita_list
from boarder_removal import get_border_removal_size
from ita_core_computations import compute_ita_from_lab
from random_patches import get_random_patches_ita_list
from structured_patches import get_structured_patches_ita_list


def get_ita(image: Image, remove_boarder: bool = True, border_removal_percentage: float = 0.04):
    """
    This function takes in an image and outputs the ITA value of image. To compute the ITA value the image needs
    to be converted from an RGB format to a LAB format type.

    :param image: input image
    :param remove_boarder: The flag to determine if the boarder should be removed
    :param border_removal_percentage: how much of the boarder to remove
    """

    # Crop image to remove the pixels from the boarder
    if remove_boarder:
        w, h = image.size
        removal_size = get_border_removal_size(image, border_removal_percentage)
        cropped_area = (removal_size, removal_size, w - removal_size, h - removal_size)
        cropped_image = image.crop(cropped_area)
    else:
        cropped_image = image

    lab = np.array(skimage.color.rgb2lab(cropped_image))

    return compute_ita_from_lab(lab)


def get_cropped_center_ita(image: Image,
                           patch_width: int = 8,
                           remove_boarder: bool = True,
                           border_removal_percentage: float = 0.04):
    """
    This is the wrapper function to calculate the ITA values for all the patches for the cropped center approach,
    and the median ITA value is selected.
    :param image: input image
    :param patch_width: The width of the patch in pixels. The patches are squares
    :param remove_boarder: The flag to determine if the boarder should be removed
    :param border_removal_percentage: The percentage of pixes that should be removed on the boarder
    :return: the computed ITA value
    """
    ita_values, indices = get_cropped_center_patches_ita_list(image, patch_width, remove_boarder,
                                                              border_removal_percentage)
    # dropping any nan computed values
    ita_values = [x for x in ita_values if not math.isnan(x)]

    return np.median(ita_values)


def get_structured_patches_ita(image: Image,
                               patch_width: int = 8,
                               remove_boarder: bool = True,
                               border_removal_percentage: float = 0.04):
    """
    This function returns the ITA value for the structured patches approach. This approach takes 1 row of patches around
    the boarder to get a selection around the lesion.

    :param image: input image
    :param patch_width: The width of the patch in pixels. The patches are squares
    :param remove_boarder: The flag to determine if the boarder should be removed
    :param border_removal_percentage: The percentage of pixes that should be removed on the boarder
    :return: the computed ITA value
    """
    ita_values, indices = get_structured_patches_ita_list(image, patch_width, remove_boarder, border_removal_percentage)
    # dropping any nan computed values
    ita_values = [x for x in ita_values if not math.isnan(x)]

    return np.median(ita_values)


def get_random_patches_ita(image: Image,
                           patch_width: int = 8,
                           remove_boarder: bool = True,
                           border_removal_percentage: float = 0.04,
                           percentage_of_random_patches=.25):
    """
    This function computes ITA value for the random patches apprach. The random patches randomly selected a percentage
    of patches and will select the median value of the set of ITA values.

    :param image: input image
    :param percentage_of_random_patches:  level of percentage the number random images should be selected
    :param patch_width: The width of the patch in pixels. The patches are squares
    :param remove_boarder: The flag to determine if the boarder should be removed
    :param border_removal_percentage: The percentage of pixes that should be removed on the boarder
    :return: the computed ITA value
    """

    ita_values, indices = get_random_patches_ita_list(image, patch_width, remove_boarder, border_removal_percentage,
                                                      percentage_of_random_patches)
    # dropping any nan computed values
    ita_values = [x for x in ita_values if not math.isnan(x)]

    return np.median(ita_values)
