class Mesin:
    def __init__(self, jenis):
        self.jenis = jenis

    def hidupkan(self):
        return f"Mesin {self.jenis} hidup"


class Penulis:
    def __init__(self, nama):
        self.nama = nama

    def info_penulis(self):
        return f"Penulis: {self.nama}"


class Mobil:
    def __init__(self, merk, mesin, penulis):
        self.merk = merk
        self.mesin = mesin      # Composition
        self.penulis = penulis  # Composition

    def info(self):
        return f"Mobil {self.merk} dengan {self.mesin.hidupkan()} ({self.penulis.info_penulis()})"


# Instansiasi
mesin = Mesin("Bensin")
penulis = Penulis("Andi")
mobil = Mobil("Honda", mesin, penulis)

print(mobil.info())
