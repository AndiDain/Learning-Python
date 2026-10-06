print("=======================================================")
print("          SELAMAT DATANG DI KEDAI KOPI ANDIDI          ")
print("=======================================================")

# Fungsi untuk stop while loop
def tanyaLanjut():
    lanjut = input("Mau pesan lagi? (y/n): ").strip().lower()
    if lanjut != "y":
        print("Terimakasih, sampai jumpa lagi!")
        return False
    return True

# while loop yang mengulang selamanya agar user bisa memesan lebih dari sekali
while True:
  # deklarasi dan inisialisasi dengan campuran hardcoded dan input
    namaPelanggan = input("Nama anda siapa: ")
    hargaAmericano = 15000
    hargaLatte = 20000

    jumlahPesananAmericano = input("Jumlah pesanan americano: ")
    jumlahPesananLatte = input("Jumlah pesanan latte: ")

    # error handling untuk input bersifat non-integer
    try:
        jumlahPesananAmericano = int(jumlahPesananAmericano)
        jumlahPesananLatte = int(jumlahPesananLatte)

    except ValueError:
        print("Harus menggunakan angka!")
        if not tanyaLanjut():
            break
        continue

    # operasi perkalian dan pertambahan, perkalian diutamakan terlebih dahulu dengan mengkalikan jumlah dengan harga lalu menambahkan 22nya
    totalHarga = (jumlahPesananAmericano * hargaAmericano) + (jumlahPesananLatte * hargaLatte)
    pembayaran = input("Masukkan pembayaran anda: ")

    try:
      pembayaran = float(pembayaran)
    except ValueError:
      print("bukan angka valid")

    finalPembayaran = round(pembayaran * 100)
    # kondisi jika pembayaran kurang dari total harga
    if finalPembayaran < totalHarga:
        print("Maaf uang anda tidak cukup")
        if not tanyaLanjut():
            break
        continue

    Kembalian = pembayaran - totalHarga

    print("=======================================================")
    print(f"Terimakasih sudah belanja di kedai kami: {namaPelanggan}")
    print(f"Total harga: {totalHarga}")
    print(f"Kembalian uang: {Kembalian}")
    print("=======================================================")

    if not tanyaLanjut():
        break
