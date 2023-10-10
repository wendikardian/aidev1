# class Siswa:
#     def __init__(self, nama, usia):
#         self.nama = nama
#         self.usia = usia

# siswa1 = Siswa("John", 18)
# siswa2 = Siswa("Alice", 17)


# class Lingkaran:
#     def __init__(self, jari_jari):
#         self.jari_jari = jari_jari

#     def hitung_luas(self):
#         return 3.14 * self.jari_jari * self.jari_jari

# lingkaran1 = Lingkaran(5)
# luas = lingkaran1.hitung_luas()


class Mobil:
    def __init__(self, merk, tahun_pembuatan):
        self.merk = merk
        self.tahun_pembuatan = tahun_pembuatan


mobil1 = Mobil("Toyota", 2022)
print(f"Merk: {mobil1.merk}, Tahun Pembuatan: {mobil1.tahun_pembuatan}")
