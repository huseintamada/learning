def hapus_pesanan():
    global daftar_pesanan
    if not daftar_pesanan:
        print("Tidak ada pesanan yang dapat dihapus.")
        return

    print("Daftar Pesanan:")
    for i, pesanan in enumerate(daftar_pesanan, start=1):
        print(f"{i}: Jenis Bahan: {pesanan['jenis_bahan']}, Panjang: {pesanan['panjang']} Meter, Lebar: {pesanan['lebar']} Meter, Total Harga: {pesanan['harga_total']}")

    nomor_pesanan = int(input("Masukkan nomor pesanan yang ingin dihapus: "))
    if 1 <= nomor_pesanan <= len(daftar_pesanan):
        pesanan_terhapus = daftar_pesanan.pop(nomor_pesanan - 1)
        print(f"Pesanan {nomor_pesanan} telah dihapus: Jenis Bahan: {pesanan_terhapus['jenis_bahan']}, Panjang: {pesanan_terhapus['panjang']} Meter, Lebar: {pesanan_terhapus['lebar']} Meter, Total Harga: {pesanan_terhapus['harga_total']}")
    else:
        print("Nomor pesanan tidak valid.")


def tambah_complain():
    global daftar_pesanan
    if not daftar_pesanan:
        print("Tidak ada pesanan untuk komplain.")
        return

    print("Daftar Pesanan:")
    for i, pesanan in enumerate(daftar_pesanan, start=1):
        print(f"{i}: Jenis Bahan: {pesanan['jenis_bahan']}, Panjang: {pesanan['panjang']} Meter, Lebar: {pesanan['lebar']} Meter, Total Harga: {pesanan['harga_total']}")

    nomor_pesanan = int(input("Masukkan nomor pesanan yang ingin diajukan komplain: "))
    if 1 <= nomor_pesanan <= len(daftar_pesanan):
        komplain = input("Masukkan komplain anda: ")
        print(f"Komplain untuk pesanan {nomor_pesanan}: {komplain}")
    else:
        print("Nomor pesanan tidak valid.")


def main():
    print("""
#####################################     
# Ujian Akhir Algoritma Pemrograman # 
#####################################      
      """)

    print("""
============================
-= Bams Digital Printing =-
============================      
          \n""")

    print("""Lagi nyari tempat cetak banner dengan harga terjangkau dan bisa ditunggu? Yaa cuma di Bams Digital Printing.
Yuk, registrasi dulu yuk...
          \n""")
    daftar = input("Nama costumer: ")
    daftar1 = daftar.upper()
    print("Selamat datang ", daftar1, ", segera buat pesanan baru agar dapat kami proses. Kami siap melayani :)\n")

    # Variabel utama
    global status_pesanan
    status_pesanan = False
    global daftar_pesanan
    daftar_pesanan = []
    global total_keseluruhan
    total_keseluruhan = 0
    kode_invoice_izinkan = ['BY021', 'QA903', 'JK999']

    while True:
        print("""
    -------------------------------------
    |   Kode    |   Jenis Layanan       |
    -------------------------------------
    |   CB01    |   Cetak Banner Baru   |
    |   AC03    |   Ambil Hasil Cetakan |
    |   PN05    |   Daftar Pesanan      |
    |   CF04    |   Cetak Faktur        |
    |   HP06    |   Hapus Pesanan       |
    |   CP07    |   Complain            |
    |   LG02    |   Keluar              |
    ------------------------------------- 
        """)

        awal = input("\n Masukkan kode layanan: ").upper()

        if awal == "CB01":
            cetak_banner()
        elif awal == "AC03":
            ambil_hasil_cetakan()
        elif awal == "PN05":
            daftar_pesanan()
        elif awal == "CF04":
            cetak_faktur()
        elif awal == "HP06":
            hapus_pesanan()
        elif awal == "CP07":
            tambah_complain()
        elif awal == "LG02":
            print("Program keluar")
            break  # Keluar dari loop dan program
        else:
            print("Kode tidak tersedia")


# Panggil fungsi utama
main()
