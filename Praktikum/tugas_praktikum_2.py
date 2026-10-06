# # KODE SALAH
# umurPenonton = 20
# 
# if umurPenonton > 12:
#     print("Kategori Tiket Remaja (Rp. 35.000)")
# elif umurPenonton > 18:
#     print("Kategori Tiket Dewasa (Rp. 50.000)")
# else:
#     print("Kategori Tiket Anak-Anak (Rp. 25.000)")
# 
# # KODE BENAR
# if umurPenonton > 18:
#     print("Kategori Tiket Dewasa (Rp. 35.000)")
# elif umurPenonton > 12:
#     print("Kategori Tiket Remaja (Rp. 50.000)")
# else:
#     print("Kategori Tiket Anak-Anak (Rp. 25.000)")

# totalBelanja = int(input("Masukkan Total Belanja Anda: "))
# totalBayar = int(input("Masukkan Pembayaran Anda"))
# tingkatMember = "Gold"
# 
# match tingkatMember:
#     case "Gold":
#         diskon = 0.20
#     case "Silver":
#         diskon = 0.10
#     case "Bronze":
#         diskon = 0.05
#     case _:
#         diskon = 0.0
# 
# totalDiskon = totalBelanja * diskon
# totalBayar = totalBelanja - totalDiskon
# 
# bonus = "Voucher Cashback" if totalBayar > 200000 else "Tidak ada bonus"
# 
# print(" ========== STRUK PEMBAYARAN ========== ")
# print(f"Total Belanja : Rp{totalBelanja}")
# print(f"Diskon        : {int(diskon*100)}%")
# print(f"Total Bayar   : Rp{totalBayar}")
# print(f"Bonus         : {bonus}")


semester = int(input("Semester Berapa : "))
ipk = float(input("IPK Berapa : "))
nilaiPemDas = input("Masukkan Nilai Anda : ")
pengalamanOrganisasi = True

if semester > 3 and (ipk > 3.50 or nilaiPemDas == 'A'):
    if pengalamanOrganisasi:
        print("Lolos Sebagai Asisten Dosen Utama")
    else:
        print("Lolos Sebagai Asisten Dosen Pendamping")

else:
    print("Maaf, Anda belum memenuhi syarat pendaftaran")