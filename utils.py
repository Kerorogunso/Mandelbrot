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

    def re(self):
        return self.real

    def im(self):
        return self.imag
    

# Calculates absolute value of a complex number.
def cabs(n):
    return n.real**2 + n.imag**2