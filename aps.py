from skimage.filters import threshold_otsu, threshold_local, try_all_threshold, threshold_yen
from skimage import io
from skimage.filters.rank import median
# from skimage.measure import label
from skimage.morphology import disk,medial_axis,remove_small_objects, label
from skimage import exposure, segmentation
from skimage.color import label2rgb, rgb2lab, rgb2gray

import matplotlib.pyplot as plt
import numpy as np

nameimg_amazon = ["amazon1.png", "amazon2.png", "amazon3.png", "amazon4.png", "amazon5.png"]
nameimg_alagada = ["alagada1.png", "alagada2.png", "alagada3.png", "alagada4.png", "alagada5.png"]

for item in nameimg_amazon:
    input_image = io.imread('images/' + item ,as_grey=False, plugin=None, flatten=None)

    imagegray = rgb2gray(input_image)
    # image = median(imagegray, disk(15)) 

    # Contrast stretching
    p2, p98 = np.percentile(imagegray, (2, 98))
    img_rescale = exposure.rescale_intensity(imagegray, in_range=(p2, p98))
    # img_eq = exposure.equalize_adapthist(imagegray)


    global_thresh = threshold_otsu(imagegray)
    binary_global = imagegray > global_thresh


    cleared = binary_global.copy()
    segmentation.clear_border(cleared)

    label_image = label(cleared)
    image_label_overlay = label2rgb(label_image, image=input_image)
    # clean_border = segmentation.clear_border(binary_global).astype(np.int)

    # edges = segmentation.mark_boundaries(imagegray, clean_border)
    # fig, ax = try_all_threshold(imagegray, figsize=(10, 8), verbose=False)
    # plt.show()


    fig2, ax = plt.subplots(2, 3, figsize=(10, 10))

    ax[0,0].imshow(input_image,cmap=plt.cm.gray)
    ax[0,0].set_title('Original')
    ax[0,0].axis('image')

    ax[0,1].imshow(imagegray, cmap=plt.cm.gray)
    ax[0,1].set_title('Grayscale')
    ax[0,1].axis('image')

    ax[0,2].imshow(img_rescale, cmap=plt.cm.gray)
    ax[0,2].set_title('Contrast stretching')
    ax[0,2].axis('image')

    ax[1,0].imshow(binary_global, cmap=plt.cm.gray)
    ax[1,0].set_title('Binaria Global com Otsu')
    ax[1,0].axis('image')

    ax[1,1].imshow(label_image, cmap=plt.cm.gray)
    ax[1,1].set_title('Labeled image')
    ax[1,1].axis('image')

    ax[1,2].imshow(image_label_overlay, cmap=plt.cm.gray)
    ax[1,2].set_title('Labeled image com overlay')
    ax[1,2].axis('image')

    # ax[1,1].imshow(label_image, cmap=plt.cm.gray)
    # ax[1,1].set_title('label_image')
    # ax[1,1].axis('image')

    plt.show()

    print "name of image: ", item, "number of components: ", len(np.unique(label_image))

    # print len(label_image)

    # ax[1,1].hist(imagegray.ravel(), bins=256)
    # ax[1,1].set_title('Grayscale histograma')
    # ax[1,1].set_xlim(0, 1)



