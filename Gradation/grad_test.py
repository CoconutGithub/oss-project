from PIL import Image,ImageDraw
from gradMethod import apply_gradation_filter


img=Image.open('Gradation/test_img.png')
filtered_img=apply_gradation_filter(img,(223,43,45),(22,143,78),'col')
filtered_img.show()