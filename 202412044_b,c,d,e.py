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
