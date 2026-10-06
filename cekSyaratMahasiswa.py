def cekSyaratMahasiswa(angkatan, ipk, status):
    if status.strip().upper() != "AKTIF":
        return False
    return (angkatan == 2025 or angkatan == 2026) and ipk >= 3.00

angkatan = input("Angkatan Berapa: ")
ipk = input("IPK Berapa: ")
nilai = input("Nilai Berapa: ")
status = input("Status Mahasiswa: ")

try:
    angkatan = int(angkatan)
    ipk = float(ipk)
    nilai = int(nilai)
except ValueError:
    print("Input invalid!, harus menggunakan angka")
    exit()

if nilai > 100 or nilai < 0:
    print("Nilai invalid, mohon untuk mengulang lagi")
elif ipk > 4.00 or ipk < 0:
    print("IPK invalid, mohon untuk mengulang lagi")
elif angkatan < 1980:
    print("Tahun angkatan tidak valid")
else:
    if cekSyaratMahasiswa(angkatan, ipk, status):
        print("Mahasiswa memenuhi persyaratan")
    else:
        print("Mahasiswa tidak memenuhi persyaratan")