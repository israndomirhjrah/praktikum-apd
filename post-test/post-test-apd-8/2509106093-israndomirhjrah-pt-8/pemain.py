from variabel import pemain, club
from prettytable import PrettyTable

def tampilkan_data_pemain(data):
    angka = 1
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Pemain", "Harga", "Club"]
    for nama, harga in data.items():
        tabel.add_row([angka, nama, f"euro{harga}", club])
        angka += 1
    print(tabel)

def tambah_pemain_baru():
    try:
        nama = input("Masukkan nama pemain baru: ")
        harga = int(input("Masukkan harga pemain: "))
        pemain[nama] = harga
        print("Pemain berhasil ditambahkan.")
    except ValueError:
        print("Harga harus berupa angka!")

def hapus_pemain():
    try:
        nama = input("Masukkan nama pemain yang ingin dihapus: ")
        if nama in pemain:
            del pemain[nama]
            print(f"Pemain {nama} berhasil dihapus.")
        else:
            print("Nama pemain tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)

def update_harga_pemain(nama_pemain, harga_baru):
    if nama_pemain in pemain:
        pemain[nama_pemain] = harga_baru
        print(f"Harga pemain {nama_pemain} telah diperbarui.")
    else:
        print("Pemain tidak ditemukan.")