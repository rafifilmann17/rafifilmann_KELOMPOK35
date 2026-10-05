def tampilkan_watermark():
    print("_" * 40)
    print("   Input Buku Perpustakaan")
    print("   Kelompok 35")
    print("_" * 40)

def tampilkan_pesan(pesan):
    print(f"[INFO] {pesan}")
def ambil_menu():
    menu = (
        "\n--- MENU ---\n"
        "1. Tambah buku\n"
        "2. Lihat daftar buku\n"
        "3. Pinjam buku\n"
        "4. Kembalikan buku\n"
        "5. Cek stok buku\n"
        "0. Keluar"
    )
    return menu
def validasi_angka(teks):
    if teks.isdigit() and int(teks) > 0:
        return int(teks)
    return -1




class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.buku = {} 

    def tambah_buku(self, judul, stok):
        if judul in self.buku:
            self.buku[judul] += stok
        else:
            self.buku[judul] = stok
        tampilkan_pesan(f"Buku '{judul}' berhasil ditambahkan (stok: {self.buku[judul]}).")

    # Method non-return, tanpa parameter
    def tampilkan_buku(self):
        if len(self.buku) == 0:
            tampilkan_pesan("Belum ada buku di perpustakaan.")
            return
        print(f"\nDaftar buku di {self.nama}:")
        nomor = 1
        for judul, stok in self.buku.items():
            print(f"{nomor}. {judul} (stok: {stok})")
            nomor += 1

    def kembalikan_buku(self, judul):
        if judul in self.buku:
            self.buku[judul] += 1
            tampilkan_pesan(f"Buku '{judul}' berhasil dikembalikan.")
        else:
            tampilkan_pesan("Buku tersebut bukan milik perpustakaan ini.")

    def cek_stok(self, judul):
        if judul in self.buku:
            return self.buku[judul]
        return -1

    def pinjam_buku(self, judul):
        stok = self.cek_stok(judul)
        if stok == -1:
            return "Buku tidak ditemukan."
        elif stok == 0:
            return "Stok buku habis."
        else:
            self.buku[judul] -= 1
            return f"Berhasil meminjam '{judul}'. Sisa stok: {self.buku[judul]}"

    # Method return, tanpa parameter
    def total_buku(self):
        total = 0
        for stok in self.buku.values():
            total += stok
        return total


def main():
    tampilkan_watermark()
    perpus = Perpustakaan("Perpustakaan Kampus")
    berjalan = True

    while berjalan:
        print(ambil_menu())
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Judul buku: ")
            stok = validasi_angka(input("Jumlah stok: "))
            if stok == -1:
                tampilkan_pesan("Stok harus berupa angka positif.")
            else:
                perpus.tambah_buku(judul, stok)

        elif pilihan == "2":
            perpus.tampilkan_buku()
            print(f"Total seluruh stok: {perpus.total_buku()}")

        elif pilihan == "3":
            judul = input("Judul buku yang dipinjam: ")
            print(perpus.pinjam_buku(judul))

        elif pilihan == "4":
            judul = input("Judul buku yang dikembalikan: ")
            perpus.kembalikan_buku(judul)

        elif pilihan == "5":
            judul = input("Judul buku: ")
            stok = perpus.cek_stok(judul)
            if stok == -1:
                tampilkan_pesan("Buku tidak ditemukan.")
            else:
                tampilkan_pesan(f"Stok '{judul}': {stok}")

        elif pilihan == "0":
            tampilkan_pesan("Terima kasih! - Kelompok XX")
            berjalan = False

        else:
            tampilkan_pesan("Pilihan tidak valid.")


main()