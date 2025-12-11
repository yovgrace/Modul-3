# Class Person
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur


# Class Buku (composition dengan Person sebagai Penulis)
class Buku:
    def __init__(self, judul, penulis: Person):
        self.judul = judul
        self.penulis = penulis   # composition

    def info_buku(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis.nama}, Umur Penulis: {self.penulis.umur}"


# Demonstrasi (akses data penulis dari objek buku)
penulis1 = Person("Rudi Hartono", 35)
buku1 = Buku("Belajar Python Dasar", penulis1)

# Akses langsung
print("Nama Penulis:", buku1.penulis.nama)
print("Umur Penulis:", buku1.penulis.umur)

# Akses melalui method
print(buku1.info_buku())
