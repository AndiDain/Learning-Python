#SOAL 1
# 
# VERSI ERROR
namaMahasiswa = "Andi"
2_nilai_tugas = 85
nilai_ujian = "90"
total = 2_nilai_tugas + nilai_ujian
print("Nilai Tugas", namaMahasiswa, "adalah", total)

#VERSI BENAR
namaMahasiswa = "Andi"
nilai_tugas = 85
nilai_ujian = 90
total = nilai_tugas + nilai_ujian
print("Hasil dari total nilai: ", total)

#SOAL2
# 
print("===== SELAMAT DATANG DI TOKO KOPI ANDIDI =====")
namaPelanggan = "Andi"
hargaAmericano = 15000
hargaLatte = 20000
jumlahPesananAmericano = 2
jumlahPesananLatte = 2
totalHarga = (jumlahPesananAmericano * hargaAmericano) + (jumlahPesananLatte * hargaLatte)
pembayaran = 100000
kembalian = pembayaran - totalHarga
print("Terimakasih sudah belanja di toko kopi Andidi", namaPelanggan)
print("Total Harga:", totalHarga)
print("Kembalian:", kembalian)

#SOAL 3
# 
angkatan = 2023
ipk = 3.5
status = True
nilai = 90
print("Mahasiswa Angkatan:", angkatan)
print("IPK:", ipk)
print("Status Mahasiswa:", status)
print("Nilai:", nilai)
lulus = (angkatan == 2024 or angkatan == 2025) and ipk >= 3.00 and status
print(lulus)