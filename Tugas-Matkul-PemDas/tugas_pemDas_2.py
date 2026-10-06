# # SOAL 1
# barang = {
#     "P001": {"Nama" : "Andi", "Barang" : "Kursi", "Harga" : 100000, "Jumlah" : 5},
#     "P002": {"Nama" : "Andidih", "Barang" : "Meja", "Harga" : 200000, "Jumlah" : 7},
#     "P003": {"Nama" : "Riva", "Barang" : "Bantal", "Harga" : 200000, "Jumlah" : 7},
# }
# 
# # ambil data di nested dict barang menggunakan fungsi items() berdasarkan kode barang
# for kode, data in barang.items():
#     # tampilkan kode barang
#     print(kode)
# 
#     # ambil dan tampilkan key dan value menggunakan fungsi items() dalam format rapih
#     for key, value in data.items():
#         print(key, ":", value)

# SOAL 2 
#Nested Array yang menyimpan data mahasiswa
mahasiswa = {
    1262001035 : {"Nama" : "Andi", "JenisKelamin" : "L", "Alamat" : "Setiabudi", "NilaiAngka" : 70},
    1262001034 : {"Nama" : "Ronaldo", "JenisKelamin" : "L", "Alamat" : "Portugal", "NilaiAngka" : 30},
    1262001030 : {"Nama" : "Messi", "JenisKelamin" : "L", "Alamat" : "Argentina", "NilaiAngka" : 100},
}

# buat list untuk rentang nilai huruf
syaratNilaiHuruf = ["A", "A-", "B+", "B", "B-", "C+", "C"]

# ambil data key dan value berdasarkan nim
for nim, data in mahasiswa.items():

    # ambil value dari key nilaiAngka
    nilai = data["NilaiAngka"]

    # cek jika nilai angka dalam batas aman
    if nilai < 0 and nilai > 100:
        data["NilaiHuruf"] = "-"
        data["NilaiAngka"] = "NILAI TIDAK VALID"
        continue

    # cek jika nilai huruf berdasarkan nilai angka
    if nilai >= 85:
        nilaiHuruf = "A"
    elif nilai >= 80:
        nilaiHuruf = "A-"
    elif nilai >= 75:
        nilaiHuruf = "B+"
    elif nilai >= 70:
        nilaiHuruf = "B"
    elif nilai >= 65:
        nilaiHuruf = "B-"
    elif nilai >= 60:
        nilaiHuruf = "C+"
    elif nilai >= 50:
        nilaiHuruf = "C"
    elif nilai >= 45:
        nilaiHuruf = "D"
    else:
        nilaiHuruf = "E"

    # tambahkan key nilaiHuruf dan value berdasarkan hasil pengkondisian diatas
    data["NilaiHuruf"] = nilaiHuruf

    if nilaiHuruf in syaratNilaiHuruf:
        data["StatusKelulusan"] = "LULUS"
    else:
        data["StatusKelulusan"] = "TIDAK LULUS"
    
# ambil data di nested dict mahasiswa menggunakan fungsi items() berdasarkan nim mahasiswa
for nim, data in mahasiswa.items():
    print(nim)
    # ambil dan tampilkan key dan value menggunakan fungsi items() dalam format rapih
    for key, value in data.items():
        print(key, ":", value)
    print()


