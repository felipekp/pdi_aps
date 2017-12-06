from skimage.filters import threshold_otsu, threshold_local
from skimage import io
from skimage.color import rgb2gray
from skimage.filters.rank import median
from skimage.morphology import disk,medial_axis,remove_small_objects

import matplotlib.pyplot as plt


input_image = io.imread('images/amazon1.png',as_grey=False, plugin=None, flatten=None)

imagegray = rgb2gray(input_image)
image = median(imagegray, disk(15)) 


global_thresh = threshold_otsu(image)
binary_global = image < global_thresh

# block_size = 711 nao vale a pena para amazon images
# adaptive_thresh = threshold_local(image, block_size, offset=1)
# binary_adaptive = image < adaptive_thresh


fig2, ax = plt.subplots(2, 2, figsize=(10, 10))

ax[0,0].imshow(input_image,cmap=plt.cm.gray)
ax[0,0].set_title('Original')
ax[0,0].axis('image')

ax[0,1].imshow(imagegray, cmap=plt.cm.gray)
ax[0,1].set_title('Grayscale')
ax[0,1].axis('image')

ax[1,0].imshow(binary_global, cmap=plt.cm.gray)
ax[1,0].set_title('Binaria global Otsu')
ax[1,0].axis('image')


ax[1,1].hist(input_image.ravel(), bins=256)
ax[1,1].set_title('Histograma')
ax[1,1].axvline(global_thresh, color='r')


plt.show()


# print ("Length 1: {0}".format(sum(sum(skel1))))
# print ("Length 2: {0}".format(sum(sum(skel2))))