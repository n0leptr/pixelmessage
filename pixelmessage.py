# Author: Gabriel De Jesus
from dataclasses import dataclass
from PIL import Image
import math


@dataclass
class Pixl:
    r: int
    g: int
    b: int


asciiz = []
message = "Can I generate a pixel image based on the ascii decimal values of each character?"

for c in message:
    p = Pixl(ord(c), ord(c), ord(c))
    asciiz.append(p)

sqr = round(math.sqrt(len(message)))
sqr += 1


def msg_to_pixels():
    img = Image.new('RGB', (sqr, sqr))
    i = 0
    # Create L x H matrix of pixels and populate it with black.
    for p in range(0, sqr):
        for q in range(0, sqr):
            img.putpixel((p, q), (0, 0, 0))
    # use each character to generate a pixel by taking it's ASCII decimal value
    for j in range(0, sqr):
        for k in range(0, 8):
            img.putpixel((j, k), (asciiz[i].r, asciiz[i].g, asciiz[i].b))
            i += 1
            if i == len(message):
                continue

    img.save('encoded.png')
    return img


pic = msg_to_pixels()
pic.show()
