from PIL import Image
import math

dense_gradient="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1] 
dg_arr = list(dense_gradient)
dg_len = len(dg_arr)
interval = dg_len / 256
scale_factor = 1
char_aspect = 0.5 

def getChar(inpInt):
    return dg_arr[min(math.floor(interval * inpInt), dg_len - 1)]

img = Image.open("strawberry.png")
width, height = img.size
img = img.resize(
    (int(scale_factor * width), int(scale_factor * height * char_aspect)),
    Image.Resampling.NEAREST
)
width, height = img.size
pix = img.load()

with open("Output.txt", 'w') as finaltxt:
    for i in range(height):
        for j in range(width):
            r, g, b, a = pix[j, i]
            h = int(0.299*r + 0.587*g + 0.114*b)
            finaltxt.write(getChar(h))
        finaltxt.write("\n")