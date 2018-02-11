from PIL import Image
import math
from utils import complex, cabs
from numpy import arctan2, cos, sin

colours = [(66, 30, 15),
    (25, 7, 26),
    (9, 1, 47),
    (4, 4, 73),
    (0, 7, 100),
    (12, 44, 138),
    (24, 82, 177),
    (57, 125, 209),
    (134, 181, 229),
    (211, 236, 248),
    (241, 233, 191),
    (248, 201, 95),
    (255, 170, 0),
    (204, 128, 0),
    (153, 87, 0),
    (106, 52, 3)]

def julia(n, rec,imc , width = 800, height = 600):
    # Create new black image
    image = Image.new('RGB', (width, height), "black")

    def convergence(re_z, im_z):
        iteration = 0
        max_iteration = 1000

        re_z = 1.5 * (re_z - width/2)/width
        im_z = 1.0 * (im_z - height/2)/height

        # While not diverging
        while re_z * re_z + im_z * im_z < 4 and iteration < max_iteration:

            xtmp = (re_z * re_z + im_z * im_z) ** (n/2) * cos(n * arctan2(im_z,re_z)) + rec
            im_z = (re_z * re_z + im_z * im_z) ** (n/2) * sin(n * arctan2(im_z,re_z)) + imc
            re_z = xtmp

            iteration += 1

        if iteration == max_iteration:
            return 100
        else:
            return iteration

    pixels = image.load()
    for i in range(width):
        for j in range(height):
            c = convergence(i * 1.0, j * 1.0)
            # pixels[i,j] = (colour << 21) + (colour << 10) + colour * 8
            pixels[i,j] = colours[c%16]
        if i%100 == 0:
            print(i)

    image.show()

if __name__ == "__main__":
    julia(2, 0.285, 0.01)
    # julia(3, -1, 0)
    # julia(4,0.6,0.55)
    # julia(2,0.279,0)


