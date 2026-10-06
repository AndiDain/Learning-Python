# # KODE SALAH
# # Data finalis bersifat tetap dan tidak dapat diubah
# finalis = ("Faalih", "Dimas", "Budi", "Budi", "Citra", "Dewi")
# 
# # 1. panitia ingin mengganti nama "Budi" dengan "Joko"
# finalis[2] = "Joko"
# 
# # 2. panitia ingin mengambil finalis pertama menggunakan slicing
# tiga_terbaik = finalis[3:]
# print(f"Tiga terbaik: {tiga_terbaik}")
# 
# 
# # Data finalis bersifat tetap dan tidak dapat diubah
# finalis = ("Faalih", "Dimas", "Budi", "Budi", "Citra", "Dewi")
# 
# # 1. panitia ingin mengganti nama "Budi" dengan "Joko"
# list_finalis = list(finalis)
# list_finalis[2] = "Joko"
# finalis = tuple(list_finalis)
# 
# 
# # 2. panitia ingin mengambil finalis pertama menggunakan slicing
# tiga_terbaik = finalis[:3]
# print(f"Tiga terbaik: {tiga_terbaik}")

# profil_mhs = {
#     "nama": "Andi",
#     "nim": "12345",
#     "matkul_terdaftar": set()
# }
# 
# pilihan_1 = ["Pemrograman Dasar", "Kalkulus", "Fisika"]
# pilihan_2 = ["Statistika", "Kalkulus", "Pemrograman Dasar", "Bahasa Inggris"]
# 
# pilihan_gabungan = pilihan_1 + pilihan_2
# pilihan_gabungan = set(pilihan_gabungan)
# 
# profil_mhs["matkul_terdaftar"] = pilihan_gabungan
# print(f"Profil mahasiswa: {profil_mhs}")

import sys

rekap_nilai = [
    [85, 90, 88],
    [78, 80, 85],
    [92, 88, 95]
]

# 1
nilai_tugas = int(input("Masukkan nilai tugas: "))
nilai_uts = int(input("Masukkan nilai UTS: "))
nilai_uas = int(input("Masukkan nilai UAS: "))

nilai = [nilai_tugas, nilai_uts, nilai_uas]

if any(nilai < 0 or nilai > 100 for nilai in nilai):
    print("Nilai tidak valid")
    sys.exit(1)

rekap_nilai.append([nilai_tugas, nilai_uts, nilai_uas])

print(f"Rekap nilai setelah ditambah: {rekap_nilai}")

# 2
mahasiswa_kedua = rekap_nilai[1][1]
print(f"Mahasiswa kedua: {mahasiswa_kedua}")

# 3
rekap_nilai[2][2] = 100
print(f"Rekap nilai setelah perubahan: {rekap_nilai}")
