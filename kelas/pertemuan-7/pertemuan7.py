# # # # # # # # def perkenalan():
# # # # # # # #   print("Halo aku Nabil")

# # # # # # # # perkenalan()


# # # # # # # def salam():
# # # # # # #  print ("halo, Ridho")
# # # # # # # def kali():

# # # # # # #     x = 5*5
# # # # # # #     print(x)
# # # # # # #     salam()
# # # # # # #     salam()
# # # # # # #     salam()
# # # # # # #     kali()
# # # # # # #     kali()
# # # # # # #     kali()

# # # # # # def nama_fungsi(parameter):
# # # # # #  print (parameter)
# # # # # # nama_fungsi("Selamat Pagi")
# # # # # #Pembuatan Fungsi Dengan Parameter
# # # # # def luas_persegi_panjang(panjang, lebar):
# # # # #     luas = panjang * lebar
# # # # #      print ("luas persegi panjang adalah ", luas)

# # # # # #Pemanggilan Fungsi luas_persegi_panjang
# # # # # luas_persegi_panjang(4, 5)
# # # # def luas_persegi(sisi):
# # # #     luas = sisi * sisi
# # # #     return luas

# # # # # pemanggilan fungsi luas persegi
# # # # print ("Luas persegi :", luas_persegi(8))
# # # # membuat variabel global
# # # Nama = "Hambali"
# # # Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

# # # # membuat variabel lokal
# # # def info():
# # #     Nama = "Informatika"
# # #     Mata_Kuliah = "Logika Informatika"

# # # # mengakses variabel lokal
# # # print("Prodi:", Nama)
# # # print("Mata Kuliah:", Mata_Kuliah)

# # # # mengakses variabel global
# # # print("Prodi:", Nama)
# # # print("Mata Kuliah:", Mata_Kuliah)

# # # # memanggil fungsi info
# # # info()

# # def faktorial(n):
# # # Basis (Base Case): Kondisi berhenti
# # if n == 1 or n == 0:
# #  return 1
# # # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
# # else:
# #     return n * faktorial(n - 1)
# # # Memanggil fungsi
# # hasil = faktorial(5)
# # print(f"Hasil dari 5! adalah: {hasil}")

# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")

    
# # Fungsi untuk mengedit data
# def edit_data():
#     show_data()
# indeks = int(input("Inputkan ID film: "))
# if indeks >= len(film) or indeks < 0:
#      print("ID salah")
# else:
#     judul_baru = input("Judul baru: ")
#     film[indeks] = judul_baru
#     print("Film berhasil diupdate!")

# def delete_data():
#     show_data()
# indeks = int(input("Inputkan ID film: "))
# if indeks >= len(film) or indeks < 0:
#     print("ID salah")
# else:
#     film.remove(film[indeks])
#     print("Film berhasil dihapus!")


