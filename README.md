# derm_ita

This library has utilities to help evaluate skin tones in dermatology images. It can be broken 
up between computing the individual typology angle(ITA) and converting the ITA value to a skin tone type.

# Computing ITA value
TODO - go into what ita is, screenshot, add equation, and boarder removal

The intended function calls will be available [here](derm_ita/derm_ita.py) 

## Full image ITA
One ITA computation is conducted on the full image regardless of any extra artifacts such as skin markings, lesions
or stickers.

## Patch approaches
Each of the following approaches will create patches of the image. Each patch will have the ITA value
computed and the median in the list will be use for the overall ITA value.

### Cropped Center
The Cropped Center approach tries to select the most of the image as possible but a portion of the 
center is removed. This is intended as many dermoscopic images have skin lesions in the center of the image
which could throw off the ITA result.

More detailed info at [Cropped Center](derm_ita/cropped_center.py#L5).

![](https://i.imgur.com/pBJbePK.png)

### Structured patches
The Structured patches approach takes the first row, the last row, first column and last column will be
    sampled for the ITA values. 

More detailed info at [Structured Patches](derm_ita/structured_patches.py#L5).

![](https://i.imgur.com/ifEwWk3.png)

### Random patches
The premise behind random patches is that a set of patches that do not overlap a generated and at random patches
    be sampled to take the ITA value from. The thought would be that because its a random sample that the majority should
    cover or represent the skin tone. It is possible that some patches could cover a skin lesion which will be address in
    a future approach.
More detailed info at [Random Patches](derm_ita/random_patches.py#L9).

![](https://i.imgur.com/9wJIkky.png)

# Skin tone classification

# Suggestions

- Best used on dermoscopic images where the image is focused on a skin lesion.

# Contribute or report issues
If you would like to contribute please submit a [Feature request](https://github.com/acorbin3/derm_ita/issues/new?assignees=&labels=&template=feature_request.md&title=).   
If you find an issue please submit a [Bug Report](https://github.com/acorbin3/derm_ita/issues/new?assignees=&labels=&template=bug_report.md&title=)