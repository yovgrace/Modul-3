import math

# Parent class
class BangunDatar:
    def luas(self):
        return 0


# b. Class Persegi yang meng-override method luas()
class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi


# b. Class Lingkaran yang meng-override method luas()
class Lingkaran(BangunDatar):
    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        return math.pi * self.radius * self.radius


# c. Demonstrasi pemanggilan method luas() dari objek masing-masing class
p = Persegi(4)
l = Lingkaran(7)

print("Luas Persegi:", p.luas())
print("Luas Lingkaran:", l.luas())
