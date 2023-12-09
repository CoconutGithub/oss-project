from PIL import Image
from MosaicFilter import apply_mosaic_filter

img=Image.open('MosaicFilter/test.jpg')
mosaic_img=apply_mosaic_filter(img,30)
mosaic_img.show()