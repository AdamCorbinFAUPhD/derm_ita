# derm_ita

This library has utilities to help evaluate skin tones in dermatology images. It can be broken 
up between computing the individual typology angle(ITA) and converting the ITA value to a skin tone type.

# Computing ITA value

The ITA value is used as a proxy to evaluate the skin tone of an image. 

The ITA uses the following equation

ITA$ = archtan \left(\frac{L - 50}{b} \right) \times \frac{180<sup>\xB0</sup>}{\pi}$

where $L$ is luminance and $b$ is amount of blue/yellow

All the approaches have the ability to remove the boarder. For those who are using these approaches
on dermoscopic datasets its advised that use the defaults to remove at least 4% of the boarder so the dark
corners will be removed for the ITA computation. 

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

More detailed info at [Cropped Center](derm_ita/cropped_center.py#L7).

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

The Fitzpatrick scale was created to classify the different skin tones. Early reasearch was around
which different skin tones were affected by sun exposure[<sup>[1]</sup>](https://onlinelibrary.wiley.com/doi/pdf/10.1111/bjd.12529).


![](https://i.imgur.com/xNYbvCl.png)

Example of fitzpatrick scale
![](https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pone.0241843/1/pone.0241843.g001.PNG_L?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20211213%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20211213T095203Z&X-Goog-Expires=86400&X-Goog-SignedHeaders=host&X-Goog-Signature=42d5d7755b000b9b13e3d8198d6eeb9d76d27868a0b5443f36e7c051e14c6e9b2b8fdf5423916c15a3697cbd4c905c59b02debb8d088abb4ec185ac6e5ca9350ac54fdd9c7a8943f4bef108627c17ee9b161635421116fd3636e7a7d66072fb9cfb64038283323146817d54c6dc1ced4d4f03cb5727706c70547a409bfa78c503dbf162d4e679eb803b5615a0498cab3de2fe5b91c750224c263f90fb824d9c434744e3a9048cc8827410cbd799432f66c80d548741557d31a250ca8f5441b3ab656a2165d7579508a13a892d1472a2d432b781d1e33d7801d806baf960ef52f56849e928d253259248e63df909b1bcf7fcc7f6babe768b924f0be62b72b5f19)


## Table 1 Fitzpatrick ranges

|ITA Range| Skin Tone Category|
|--|--|
|55$<sup>\xB0</sup> <$ ITA | Type1|
|41$<sup>\xB0</sup><$ ITA $\leq$ 55$<sup>\xB0</sup>$|Type2|
|28$<sup>\xB0</sup><$ ITA $\leq$ 41$<sup>\xB0</sup>$|Type3|
|19$<sup>\xB0</sup><$ ITA $\leq$ 28$<sup>\xB0</sup>$|Type4|
|10$<sup>\xB0</sup><$ ITA $\leq$ 19$<sup>\xB0</sup>$|Type5|
|ITA $\leq$ 10$<sup>\xB0</sup>$|Type6|

## Table 2 Groh ranges

|ITA Range| Skin Tone Category|
|--|--|
|40$<sup>\xB0</sup> <$ ITA | Type1|
|23$<sup>\xB0</sup><$ ITA $\leq$ 40$<sup>\xB0</sup>$|Type2|
|12$<sup>\xB0</sup><$ ITA $\leq$ 23$<sup>\xB0</sup>$|Type3|
|0$<sup>\xB0</sup><$ ITA $\leq$ 12$<sup>\xB0</sup>$|Type4|
|-25$<sup>\xB0</sup><$ ITA $\leq$ 0$<sup>\xB0</sup>$|Type5|
|ITA $\leq$ -25$<sup>\xB0</sup>$|Type6|

[Groh source](https://openaccess.thecvf.com/content/CVPR2021W/ISIC/papers/Groh_Evaluating_Deep_Neural_Networks_Trained_on_Clinical_Images_in_Dermatology_CVPRW_2021_paper.pdf)

## Kinyanjui ranges

|ITA Range| Skin Tone Category|
|--|--|
|55$<sup>\xB0</sup> <$ ITA | Very Light|
|48$<sup>\xB0</sup><$ ITA $\leq$ 55$<sup>\xB0</sup>$|Light 2|
|41$<sup>\xB0</sup><$ ITA $\leq$ 48$<sup>\xB0</sup>$|Light 1|
|34.5$<sup>\xB0</sup><$ ITA $\leq$ 41$<sup>\xB0</sup>$|Intermediate 2|
|28$<sup>\xB0</sup><$ ITA $\leq$ 34.5$<sup>\xB0</sup>$|Intermediate 1|
|18$<sup>\xB0</sup><$ ITA $\leq$ 28$<sup>\xB0</sup>$|Tan2|
|10$<sup>\xB0</sup><$ ITA $\leq$ 18$<sup>\xB0</sup>$|Tan1|
|ITA $\leq$ 10$<sup>\xB0</sup>$|Dark|

[Kinyanjui source](http://krvarshney.github.io/pubs/KinyanjuiOCCPSV_miccai2020.pdf)

## Del Bino ranges
|ITA Range| Skin Tone Category|
|--|--|
|55$<sup>\xB0</sup> <$ ITA | Very Light|
|41$<sup>\xB0</sup><$ ITA $\leq$ 55$<sup>\xB0</sup>$|Light|
|28$<sup>\xB0</sup><$ ITA $\leq$ 41$<sup>\xB0</sup>$|Intermediate|
|10$<sup>\xB0</sup><$ ITA $\leq$ 28$<sup>\xB0</sup>$|Tan|
|-30$<sup>\xB0</sup><$ ITA $\leq$ 10$<sup>\xB0</sup>$|Brown|
|ITA $\leq$ -30$<sup>\xB0</sup>$|Dark|

[Del Bino source](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0241843)

# Suggestions

- Best used on dermoscopic images where the image is focused on a skin lesion.

# Contribute or report issues
If you would like to contribute please submit a [Feature request](https://github.com/acorbin3/derm_ita/issues/new?assignees=&labels=&template=feature_request.md&title=).   
If you find an issue please submit a [Bug Report](https://github.com/acorbin3/derm_ita/issues/new?assignees=&labels=&template=bug_report.md&title=)