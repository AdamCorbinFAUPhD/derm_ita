import math

import numpy as np
from PIL import Image
from ita_core_computations import format_image_and_get_lab_patches, compute_ita_from_lab


# randomly pick numbers between 0 and max patches
def get_random_patches_ita_list(image: Image,
                                patch_width: int = 8,
                                remove_boarder: bool = True,
                                border_removal_percentage: float = 0.04,
                                percentage_of_random_patches=.25,
                                verbose=False):
    """
    The premise behind random patches is that a set of patches that do not overlap a generated and at random patches
    be sampled to take the ITA value from. The thought would be that because its a random sample that the majority should
    cover or represent the skin tone. It is possible that some of the patches could cover a skin lesion which will be address in
    a future approach.

    :param image: input image
    :param patch_width: The width of the patch in pixels. The patches are squares
    :param remove_boarder: The flag to determine if the boarder should be removed
    :param border_removal_percentage: The percentage of pixes that should be removed on the boarder
    :param percentage_of_random_patches: level of percentage the number random images should be selected
    :param verbose:
    :return:
    """
    patches = format_image_and_get_lab_patches(image, patch_width, remove_boarder, border_removal_percentage)
    row_count = len(patches)
    column_count = len(patches[0])

    patch_count = row_count * column_count

    random_to_select = int(patch_count * percentage_of_random_patches)

    # Generate a random list of numbers with no duplicates
    random_patch_indexes = np.random.choice(patch_count, size=random_to_select, replace=False)
    random_patch_indexes.sort()

    # get reverse indexes. The index number comes from nRow * col_count + nCol.
    # so for example if you have 10x10 image. image index 23 is row 2 col 4. The formula would be 2*10 + 4 = 24
    # x = number % column_count
    # y = int(number / column_count)

    coordinate_indices = []
    for index in random_patch_indexes:
        y = index % column_count
        x = int(index / column_count)
        coordinate_indices.append([x, y])
    if verbose:
        print(f"row_count {row_count} column_count {column_count} ")
        print(f"patch_count {patch_count}, random_to_select {random_to_select}")
        # print(f"random_patch_indexes\n{random_patch_indexes}")
        # print(f"coordinate_indices\n{coordinate_indices}")

    ita_values = []
    for index in coordinate_indices:
        x = index[1]
        y = index[0]
        patch = patches[y][x]
        ita_values.append(compute_ita_from_lab(patch[0]))

    return ita_values, coordinate_indices
