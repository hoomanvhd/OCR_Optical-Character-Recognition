
import os, sys

try:
    from PIL import Image
except ImportError:
    import Image

import glob
import pytesseract

img = []
file = "/home/hoomanvhd/Desktop/lsiTester/5/Frames/*.png"
for image in sorted(glob.glob(file)):
    img.append(Image.open(image))



with open("/home/hoomanvhd/Desktop/lsiTester/5/OCRtext.txt", "w") as textFile:
    for picture in img:
        textFile.write(pytesseract.image_to_string(picture))


# script = sys.argv[0]
# filename = sys.argv[1]
#
# DirectPath = os.path.dirname(filename)
#
# os.mkdir(DirectPath + "/Frames")
#
# FilePath = os.path.dirname(DirectPath + "/Frames")
#
# VideoName = os.path.basename(filename)
#
# os.system("ffmpeg -i " + VideoName + " -vf fps=1 Frames/frame%05d.png -hide_banner")
#
#
