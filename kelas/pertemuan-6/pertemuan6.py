# # buah = {"apel", "jeruk", "mangga", "apel"}
# # print(buah)

# # angka_ganjil = {1, 3, 5, 7, 9}
# # for angka in angka_ganjil:
# #  print(angka)

# # Daftar_buku = {
# # "Buku1" : "Bumi Manusia",
# # "Buku2" : "Laut Bercerita"
# # }
# # print(Daftar_buku["Buku1"])
# # for key in Daftar_buku.values():
# #     print(key)

# # for key in Daftar_buku.keys():
# #     print(key)

# # Biodata = {
# # "Nama" : "Ananda Daffa Harahap",
# # "NIM" : 2409106050,
# # "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# # "Mahasiswa_Aktif" : True,
# # "Social Media" : {"Instagram" : "daffahrhap"}
# # }

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# #Setelah Ditambah
# print(Film)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# del data["Nama"]
# print(data)
Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
 print(f"Musik milik {i} adalah : ")
for song in j: 
 print(song)
 print("")
