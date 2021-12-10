# Different approaches
import math

import numpy as np
from PIL import Image

from cropped_center import get_cropped_center_patches_ita_list
from derm_ita.random_patches import get_random_patches_ita_list
from structured_patches import get_structured_patches_ita_list


def get_cropped_center_ita(image: Image):
    """
    This is the wrapper function to calculate the ITA values for all the patches, the median ITA value and
    stores all the patch indices for each Image of the dataset.
    :param image: input image
    """
    ita_values, indices = get_cropped_center_patches_ita_list(image)
    # dropping any nan computed values
    ita_values = [x for x in ita_values if not math.isnan(x)]

    return np.median(ita_values)


def get_structured_patches_ita(image: Image):
    """
    This function is intended to add the ITA represented value dataframe for an instance.
    Its intended to be used with the df.swifter.apply() method
    :param image: input image
    """
    ita_values, indices = get_structured_patches_ita_list(image)
    # dropping any nan computed values
    ita_values = [x for x in ita_values if not math.isnan(x)]

    return np.median(ita_values)


def get_random_patches_ita(image: Image, percentage_of_random_patches=.25):
    """
    This function is intended to add the ITA represented value dataframe for an instance.
    Its intended to be used with the df.swifter.apply() method
    :param image: input image
    :param percentage_of_random_patches:  level of percentage the number random images should be selected
    :return: the computed ITA value
    """

    ita_values, indices = get_random_patches_ita_list(image, percentage_of_random_patches)
    # dropping any nan computed values
    ita_values = [x for x in ita_values if not math.isnan(x)]

    return np.median(ita_values)
