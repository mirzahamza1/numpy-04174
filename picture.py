from PIL import Image
img = Image.open('dp.jpg')
print(img.format)
print(img.mode)
print(img.size)
img.show()

from PIL import Image
im = Image.open("dp.jpg")

crop_centre = (100, 100, 100, 100)
cropped_im = im.crop(crop_centre)

cropped_im.show()