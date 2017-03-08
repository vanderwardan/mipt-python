from sys import stdin


class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, another):
        return ComplexNumber(self.real + another.real,
                             self.imaginary + another.imaginary)

    def __sub__(self, another):
        return ComplexNumber(self.real - another.real,
                             self.imaginary - another.imaginary)

    def __mul__(self, another):
        return ComplexNumber(
            self.real * another.real - self.imaginary * another.imaginary,
            self.real * another.imaginary + self.imaginary * another.real)

    def __truediv__(self, another):
        sqr = another.sqr()
        tmp = self * ComplexNumber(another.real, -another.imaginary)
        return ComplexNumber(tmp.real / sqr, tmp.imaginary / sqr)

    def __str__(self):
        if self.imaginary == 0:
            return "%.2f" % self.real
        elif self.real == 0:
            return "%.2fi" % self.imaginary
        else:
            if self.imaginary > 0:
                return "%.2f + %.2fi" % (self.real, self.imaginary)
            else:
                return "%.2f - %.2fi" % (self.real, abs(self.imaginary))

    def sqr(self):
        return (self.real ** 2) + (self.imaginary ** 2)

    pass


for line in stdin.readlines():
    print(eval(line.strip()))
