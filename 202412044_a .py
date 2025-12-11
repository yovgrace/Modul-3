class Burung:
    def terbang(self):
        return "Burung terbang tinggi"


class Pesawat:
    def terbang(self):
        return "Pesawat lepas landas"


def uji_terbang(obj):
    print(obj.terbang())


# Duck typing dalam aksi
b = Burung()
p = Pesawat()

uji_terbang(b)
uji_terbang(p)


# ===========================
# Tambahan: Laptop & Smartphone
# ===========================

class Laptop:
    def nyalakan(self):
        return "Laptop menyala"


class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala"


# Demonstrasi pemanggilan
l = Laptop()
s = Smartphone()

print(l.nyalakan())
print(s.nyalakan())