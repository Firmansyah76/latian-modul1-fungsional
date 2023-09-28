# Inisialisasi data peserta
data_peserta = []

# Fungsi untuk menambahkan data peserta
def tambah_peserta():
    nama = input("Masukkan Nama Peserta: ")
    nilai = float(input("Masukkan Nilai Peserta: "))
    hasil_akhir = "Lolos" if nilai >= 75 else "Tidak Lolos"
    data_peserta.append({"ID": len(data_peserta), "Nama": nama, "Nilai": nilai, "Hasil Akhir": hasil_akhir})
    print("Data Peserta Telah Ditambahkan!")

# Fungsi untuk mengedit nilai peserta
def edit_nilai():
    id_peserta = int(input("Masukkan ID Peserta yang akan diedit: "))
    if id_peserta < 0 or id_peserta >= len(data_peserta):
        print("ID Peserta tidak valid.")
        return

    nilai_baru = float(input("Masukkan Nilai Baru Peserta: "))
    hasil_akhir = "Lolos" if nilai_baru >= 75 else "Tidak Lolos"
    data_peserta[id_peserta]["Nilai"] = nilai_baru
    data_peserta[id_peserta]["Hasil Akhir"] = hasil_akhir
    print("Nilai Peserta Telah Diupdate!")

# Fungsi untuk menampilkan data peserta
def tampilkan_data_peserta(id_akun):
    if id_akun == "admin":
        for peserta in data_peserta:
            print(f"ID: {peserta['ID']}, Nama: {peserta['Nama']}, Nilai: {peserta['Nilai']}, Hasil Akhir: {peserta['Hasil Akhir']}")
    elif id_akun == "peserta":
        id_peserta = int(input("Masukkan ID Anda: "))
        if id_peserta < 0 or id_peserta >= len(data_peserta):
            print("ID Peserta tidak valid.")
            return
        peserta = data_peserta[id_peserta]
        print(f"ID: {peserta['ID']}, Nama: {peserta['Nama']}, Nilai: {peserta['Nilai']}, Hasil Akhir: {peserta['Hasil Akhir']}")

# Fungsi utama
def main():
    while True:
        print("\nSistem Informasi")
        print("1. Tambah Peserta (Admin)")
        print("2. Edit Nilai (Admin)")
        print("3. Tampilkan Data Peserta (Admin/Peserta)")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            tambah_peserta()
        elif pilihan == "2":
            edit_nilai()
        elif pilihan == "3":
            id_akun = input("Masukkan ID Akun (admin/peserta): ")
            tampilkan_data_peserta(id_akun)
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
