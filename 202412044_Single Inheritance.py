class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Kendaraan: {self.merk} ({self.tahun})"


class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_pintu):
        super().__init__(merk, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        return f"Mobil: {self.merk}, {self.jumlah_pintu} pintu ({self.tahun})"


# Instansiasi
k = Kendaraan("Yamaha", 2020)
m = Mobil("Toyota", 2022, 4)

print(k.info())
print(m.info())
# b. Class Person
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}"


# c. Class Mahasiswa yang mewarisi Person + atribut nim
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        # d. Gunakan super() untuk inisialisasi parent class
        super().__init__(nama, umur)
        self.nim = nim

    # Override method info()
    def info(self):
        return f"Mahasiswa: {self.nama}, Umur: {self.umur}, NIM: {self.nim}"


# e. Instansiasi objek dan panggil info()
p = Person("Andi", 30)
m = Mahasiswa("Budi", 20, "23120201")

print(p.info())
print(m.info())
