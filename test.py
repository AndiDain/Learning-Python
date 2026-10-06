data_mahasiswa = {"1262001021":{"nama":"Fachriz", "jenis_kelamin":"L", "alamat":"Jakarta Timur", "nilai_angka":90},
                  "1230998789":{"nama":"Auditore", "jenis_kelamin":"L", "alamat":"Bandung Utara", "nilai_angka":56},
                  "1218767978":{"nama":"Ladesh", "jenis_kelamin":"P", "alamat":"Bandung Selatan", "nilai_angka":72},
                  "1209873789":{"nama":"Rina", "jenis_kelamin":"P", "alamat":"Ngawi Selatan", "nilai_angka":34},
                  "1249045890":{"nama":"O'neal", "jenis_kelamin":"L", "alamat":"Jakarta Barat", "nilai_angka":89}}

for nim, data in data_mahasiswa.items():
    nilai = data["nilai_angka"]

    if nilai >=85:
        kelulusan_huruf="A"
    elif nilai >=80:
        kelulusan_huruf="A-"
    elif nilai >=75:
        kelulusan_huruf="B+"
    elif nilai >=70:
        kelulusan_huruf="B"
    elif nilai >=65:
        kelulusan_huruf="C+"
    elif nilai>=60:
        kelulusan_huruf="C"
    elif nilai>=50:
        kelulusan_huruf="D"
    else:
        kelulusan_huruf="E"
        
    if kelulusan_huruf == "D" or kelulusan_huruf == "E":
        status_kelulusan="TIDAK LULUS"
    else:
        status_kelulusan="LULUS"
    data["nilai_huruf"] = kelulusan_huruf
    data["status_kelulusan"] = status_kelulusan

for nim, data in data_mahasiswa.items():
    print(nim)
    for key, value in data.items():
        print(key, ":", value)
    print()

