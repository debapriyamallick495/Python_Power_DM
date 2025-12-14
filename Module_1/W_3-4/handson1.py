# Hands On 1 : image data as array
import numpy as np
from PIL import Image

path = 'Module_1/W_3-4/assets/'

#r(0-256) G(0-256) B(0-256)
#Cyan Magenta Yellow K-Black CMYK

img_arr = np.random.randint(0, 256, size=(100, 150, 3), dtype=np.uint8)

np.save(path+'synthesis_image.npy', img_arr)

load_img = np.load(path+'synthesis_image.npy')
print(f"Image shape: {load_img.shape}")
print(f"Image Data Types: {load_img}")

image = Image.fromarray(load_img)
image.save(path+'synthesis_image.png')