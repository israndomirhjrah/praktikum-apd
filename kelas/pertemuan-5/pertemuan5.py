# # # # # tuple awal
# # # # studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
# # # # # Ubah tuple menjadi list
# # # # liststudy=list(studyclub)
# # # # # Tambahkan Web
# # # # liststudy.insert(2,"Web")
# # # # # ubah kembali list menjadi tuple
# # # # studyclub=tuple(liststudy)
# # # # print(studyclub)

# # # # tuple awal
# # # studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
# # # print(studyclub)
# # # # Ubah tuple menjadi list
# # # liststudy=list(studyclub)
# # # # Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
# # # liststudy[2] = "AI"
# # # # ubah kembali list menjadi tuple
# # # studyclub=tuple(liststudy)
# # # print(studyclub)
# # # tuple awal
# # # hobi=("Futsal","Catur","Renang")
# # # print(hobi)
# # # # ubah tuple menjadi list
# # # gemar=list(hobi)
# # # # menghapus elemen pada indeks ke-2, yakni "Renang"
# # # del gemar[2]
# # # # Ubah list kembali menjadi tuple
# # # hobi=tuple(gemar)

# # # tuple
# # matakuliah = ('PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# # 'Orsikom','Basis Data')
# # # Menampilkan tuple mulai dari indeks 1 hingga 4 dengan loncatan 2
# # print(matakuliah[1:5:2])

# matakuliah = ('PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# 'Orsikom','Basis Data')
# # Menampilkan tuple mulai dari indeks 1 hingga 4 dengan loncatan 2
# print(matakuliah[::2])

mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# perulangan for untuk mendapatkan semua elemen
for i in mahasiswa:
  for j in i :
    print (j)