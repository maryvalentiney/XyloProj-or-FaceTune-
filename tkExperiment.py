from PIL import Image
import sys

try:
    image = Image.open("belldash.jpg")
except IOError:
    print("Unable to load image")
    sys.exit(1)

image.show()