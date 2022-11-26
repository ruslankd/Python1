class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        a1 = self.real
        b1 = self.imaginary
        a2 = other.real
        b2 = other.imaginary
        return Complex(a1 * a2 - b1 * b2, a1 * b2 + b1 * a2)

    def __str__(self):
        i_part = self.imaginary
        if i_part > 0:
            return f"{self.real} + {self.imaginary}j"
        elif i_part < 0:
            return f"{self.real} - {abs(self.imaginary)}j"
        else:
            return f"{self.real}"


c1 = Complex(4, 0)
c2 = Complex(-1, -2)
print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c1 + c2 = {c1 + c2}")
print(f"c1 * c2 = {c1 * c2}")
