from PIL import Image
from ita_core_computations import format_image_and_get_lab_patches, compute_ita_from_lab


def get_cropped_center_patches_ita_list(image: Image, verbose=False):
    """
    For the structure patches approach the first row, the last row, first column and last column will be
    sampled for the ITA values.

    Note we want to ignore the center part of the images. We will take a percentage_of_random_patches around the center of the image
    and ignore getting the ITA values for those images. Taking 15% of the width and height will get offset value.
    Then dividing the width and height by 2 will be the mid-point which we can take the offset and do a +-
    to get a range where we dont want to capture the ITA values as long as the x and y indexes dont fall between
    both ranges then we will capture the ITA values of the image.
    :param image: input image
    """
    patches = format_image_and_get_lab_patches(image)

    center_removal_percentage = .70 / 2
    h = len(patches)
    w = len(patches[0])

    w_offset = math.floor(w * center_removal_percentage)
    h_offset = math.floor(h * center_removal_percentage)

    w_mid = int(w / 2)
    h_mid = int(h / 2)

    indices = []

    if verbose:
        print("Will ignore values in these ranges")
        print("center_removal_percentage", center_removal_percentage)
        print("w", w)
        print("h", h)
        print("w_offset", w_offset)
        print("h_offset", h_offset)
        print("w_mid", w_mid)
        print("h_mid", h_mid)
        w_range = (w_mid + w_offset) - (w_mid - w_offset)
        print(f"w range diff {w_range} : % {w_range / w}")
        h_range = (h_mid + h_offset) - (h_mid - h_offset)
        print(f"h range diff {h_range} : %{h_range / h}")
        print(f"{w_mid - w_offset} <= x < {w_mid + w_offset} and {h_mid - h_offset} <= y < {h_mid + h_offset}")
    selected_ita_values = []
    for y, y_item in enumerate(patches):
        for x, x_item in enumerate(patches[y]):
            if w_mid - w_offset <= x < w_mid + w_offset and h_mid - h_offset <= y < h_mid + h_offset:
                continue
            patch = patches[y][x][0]
            selected_ita_values.append(compute_ita_from_lab(patch))
            indices.append([y, x])

    return selected_ita_values, indices
