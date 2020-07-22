import math


class ComplexNumbers(object):
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def add(self, other):
        if self.img + other.img > 0:
            print(str(self.real + other.real) +"+" + str(self.img + other.img) + "i")
        else:
            print(str(self.real + other.real) + str(self.img + other.img)+"i")

    def sub(self, other):
        if self.img - other.img > 0:
            print(str(self.real - other.real) + "+" + str(self.img - other.img) + "i")
        else:
            print(str(self.real - other.real) + str(self.img - other.img)+"i")

    def modulus(self):
        new = math.sqrt(self.real ** 2 + (self.img ** 2))
        print(new)

    def mul(self, other):
        if (self.img * other.real) + (self.real * other.img) > 0:
            print(str((self.real * other.real) - (self.img * other.img)) + "+" + str((self.img * other.real) + (self.real * other.img)) + "i")
        else:
            print(str((self.real * other.real) - (self.img * other.img)) + str((self.img * other.real) + (self.real * other.img))+"i")

    def conjugate(self):
        if self.img >= 0:
            print(str(self.real) + "-" + str(self.img) + "i")
        else:
            print(str(self.real)+ "+" + str(self.img)*-1 + "i")

    def display(self):
        if self.img >= 0:
            print(str(self.real) +"+" + str(self.img)+'i')
        else:
            print(str(self.real) + str(self.img) + 'i')

    def inverse(self):
        str(self.conjugate()) + str(self.modulus())
