import sys

from PIL import Image

images = []

for arg in sys.argv:
    image = Image.open(arg)
    imaeges.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images =[1], duration=200, loop=0
)