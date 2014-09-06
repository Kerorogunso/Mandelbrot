from PIL import Image
import math

# Complex number class.
class complex(object):

	def __init__(self,real,imag):
		self.real = real
		self.imag = imag
	
	# Defines addition of complex numbers.
	def add(a,b):
		re = a.real + b.real
		im = a.imag + b.imag
		return complex(re,im)
	
	# Defines multiplication of complex numbers.
	def multiply(a,b):
		re = (a.real * b.real) - (a.imag * b.imag)
		im = (a.real * b.imag) + (a.imag * b.real)
		return complex(re,im)
	

# Calculates absolute value of a complex number.
def cabs(n):
	return n.real**2 + n.imag**2

escape_radius = 3
max_iter = 1000
# Convergence test to determine elements in the Mandelbrot set.
def mandelbrot(n):
	z = complex(0,0)
	for i in range(max_iter):
		z = complex.add(complex.multiply(z,z),n)
		if cabs(z) >= escape_radius:
			smooth = i + 1 - int(math.log1p(math.log1p(cabs(z)))/math.log1p(escape_radius))
			return int(smooth)
	return True

def num_to_colour(n):
	if n >= 765:
		return [255,255,255]
	elif n >= 511:
		return [255,255,n-510]
	elif n >= 256:
		return [255,n-255,0]
	else:
		return [n,0,0]
	
# Dimension of image to produce graph starting from -2-i to 1+i.
width = 2500
height = 2500
cwidth = 2*width/3
cheight = height/2
# Number of pixels from 0 to 1
numpix = width/3.0

# Creates a black image.
img = Image.new( 'RGB', (width,height), "black")
pixels = img.load()

for i in range(img.size[0]):
	for j in range(img.size[1]):
		number = complex(((i-cwidth)/numpix),((j - cheight)/numpix))
		in_set = mandelbrot(number)
		if in_set != True:
			colour = num_to_colour(in_set)
			pixels[i,j] = (colour[0],colour[1],colour[2])

# Displays the image.

img.save('Mandelbrot.png')
img.show()
