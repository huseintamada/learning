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
status_pesanan = False
daftar_pesanan = []
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
|   LG02    |   Keluar              |
------------------------------------- 
    """)

    awal = input("\n Masukkan kode layanan: ").upper()

    if awal == "CB01":
        print("""
----------------------------------------------
|   Kode    |   Jenis Bahan  |  Harga/Meter  |
----------------------------------------------
|   AB01    |   Albatros     |  Rp. 10.200   |
|   LS02    |   Luster       |  Rp. 20.000   |
|   FK05    |   Flexy Korea  |  Rp. 15.500   |
----------------------------------------------
              """)

        # Jenis Bahan
        JB = input("Masukkan kode jenis bahan: ").upper()
        if JB == "AB01" or JB == "LS02" or JB == "FK05":
            bahan = 10200 if JB == "AB01" else (20000 if JB == "LS02" else 15500)
        else:
            print("Mohon maaf, pilihan tidak valid")
            continue  # Kembali ke menu awal
        # proses menghitung
        panjang_meter = int(input("Panjang Meter: "))
        lebar_meter = int(input("Lebar Meter: "))
        harga_total = (panjang_meter * lebar_meter) * bahan
        print("Harga Total : Rp.", harga_total)

        # Update status pesanan menjadi True
        status_pesanan = True

        # Tambahkan pesanan ke daftar_pesanan
        pesanan = {
            'jenis_bahan': JB,
            'panjang': panjang_meter,
            'lebar': lebar_meter,
            'harga_total': harga_total
        }
        daftar_pesanan.append(pesanan)

        # Update total keseluruhan
        total_keseluruhan += harga_total

    elif awal == "AC03":
        # Masukkan kode invoice
        kode_invoice = input("Masukkan kode invoice: ").upper()
        if kode_invoice in kode_invoice_izinkan:
            print(f"Cetak banner dengan nomor invoice {kode_invoice} sudah selesai diproses, Terimakasih")
        else:
            print("Kode invoice tidak terdeteksi, silahkan order cetakan baru.")
            
    elif awal == "PN05":
        # Periksa status pesanan
        if status_pesanan:
            print("Daftar Pesanan:")
            for i, pesanan in enumerate(daftar_pesanan, start=1):
                print(f"{i}: Daftar pesanan anda: {pesanan['jenis_bahan']}, Total Harga: {pesanan['harga_total']}")
            print(f"Total Keseluruhan: Rp. {total_keseluruhan}")
            
            # diskon 10% jika total keseluruhan lebih dari 300 ribu
            if total_keseluruhan > 300000:
                diskon = 0.1 * total_keseluruhan
                total_keseluruhan -= diskon
                print(f"Selamat!!! Diskon 10% diberikan! Total Keseluruhan setelah diskon: Rp. {total_keseluruhan}")
        else:
            print("Maaf, Anda belum membuat pesanan.")

    elif awal == "LG02":
        print("Program keluar")
        break  # Keluar dari loop dan program
    else:
        print("Kode tidak tersedia")
