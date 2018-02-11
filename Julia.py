from PIL import Image
import math
from utils import complex, cabs
from numpy import arctan2, cos, sin

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
            colour = convergence(i * 1.0, j * 1.0)
            pixels[i,j] = (colour << 21) + (colour << 10) + colour * 8
        if i%100 == 0:
            print(i)

    image.show()

if __name__ == "__main__":
    # julia(2, 0.285, 0.01)
    # julia(3, -1, 0)
    # julia(4,0.6,0.55)
    julia(2,0.279,0)


