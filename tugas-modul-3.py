# 1. Class Parent: Karyawan
class Karyawan:
    def _init_(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        """Method untuk menampilkan gaji pokok."""
        return f"Nama: {self.nama}, Gaji Pokok: Rp{self.gaji_pokok:,.0f}"

# 2. Child Class: Manager (inherits Karyawan)
class Manager(Karyawan):
    def _init_(self, nama, gaji_pokok, tunjangan):
        # Menggunakan super() untuk inisialisasi atribut Parent Class
        super()._init_(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):
        """Override method: menampilkan Gaji Total (Gaji Pokok + Tunjangan)."""
        gaji_total = self.gaji_pokok + self.tunjangan
        return (f"Jabatan: Manager\n"
                f"Nama: {self.nama}\n"
                f"Gaji Pokok: Rp{self.gaji_pokok:,.0f}\n"
                f"Tunjangan: Rp{self.tunjangan:,.0f}\n"
                f"Gaji Total: Rp{gaji_total:,.0f}")

# 3. Child Class: Programmer (inherits Karyawan)
class Programmer(Karyawan):
    def _init_(self, nama, gaji_pokok, bonus):
        # Menggunakan super() untuk inisialisasi atribut Parent Class
        super()._init_(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):
        """Override method: menampilkan Gaji Total (Gaji Pokok + Bonus)."""
        gaji_total = self.gaji_pokok + self.bonus
        return (f"Jabatan: Programmer\n"
                f"Nama: {self.nama}\n"
                f"Gaji Pokok: Rp{self.gaji_pokok:,.0f}\n"
                f"Bonus: Rp{self.bonus:,.0f}\n"
                f"Gaji Total: Rp{gaji_total:,.0f}")

# 4. Composition: Class Departemen
class Departemen:
    def _init_(self, nama_dept):
        self.nama_dept = nama_dept
        self.daftar_karyawan = [] # Composition: Departemen memiliki daftar Karyawan

    def tambah_karyawan(self, karyawan):
        """Method untuk menambahkan objek Karyawan ke daftar."""
        self.daftar_karyawan.append(karyawan)
        print(f"✅ {karyawan.nama} berhasil ditambahkan ke Departemen {self.nama_dept}.")

    def tampilkan_karyawan(self):
        """Method untuk menampilkan info gaji semua karyawan dalam departemen."""
        print(f"\n==============================================")
        print(f"DAFTAR KARYAWAN DEPARTEMEN {self.nama_dept.upper()}")
        print(f"==============================================")
        
        if not self.daftar_karyawan:
            print("Belum ada karyawan di departemen ini.")
            return

        for karyawan in self.daftar_karyawan:
            print("-" * 30)
            # Polimorfisme dalam aksi: Memanggil info_gaji() yang berbeda
            print(karyawan.info_gaji())
        print("-" * 30)
        print("==============================================")

# 5. Instansiasi dan Demonstrasi

# Instansiasi objek Karyawan (Manager dan Programmer)
print("--- Proses Instansiasi Karyawan ---")
manager1 = Manager("helwina destiana putri", 8000000, 2000000)
manager2 = Manager("yovitha gracia tavares", 8500000, 2500000)
programmer1 = Programmer("nazwa putri elina", 6000000, 1500000)
programmer2 = Programmer("fatimah az zahra", 6200000, 1800000)

# Instansiasi objek Departemen
dept_it = Departemen("Teknologi Informasi")

# Tambahkan Karyawan ke Departemen
print("\n--- Menambahkan Karyawan ke Departemen ---")
dept_it.tambah_karyawan(manager1)
dept_it.tambah_karyawan(manager2)
dept_it.tambah_karyawan(programmer1)
dept_it.tambah_karyawan(programmer2)

# Tampilkan info gaji semua karyawan
dept_it.tampilkan_karyawan()