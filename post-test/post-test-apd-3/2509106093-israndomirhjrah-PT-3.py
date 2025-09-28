#data pengguna
data={"israndomirhjrah",2509106093}


nama=input("Masukkan Nama:")
nim=int(input("Masukkan Nim:"))

if nama in data and nim in data:
       print("Login Berhasil")
       print("")
       print("======Menu Langganan======")
       print("")
       print("Langganan Aplikasi Streaming Musik Seharga Rp 1.500.000")
       print("") 
       print("1.Paket Bronze: Biaya administrasi 1%, akses dasar ke lagu-lagu populer.")
       print("2.Paket Silver: Biaya administrasi 3%, akses lagu premium dan playlist kustom.")
       print("3.Paket Gold: Biaya administrasi 5%, akses lagu premium, playlist kustom, dan mode offline.")
       print("4.Paket Platinum: Biaya administrasi 7%, akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis.")
       print("")
       pilih=int(input("Pilih Paket Yang Anda Inginkan:"))
       print("")

       biaya=1500000

       if pilih ==1:
              biaya_admin= biaya * 1/100
              bronze= biaya + biaya_admin
              print(f"Untuk Harga Paket Bronze Dan Biaya Administrasinya jadi:{bronze}")
              print("Dengan Keuntungan Akses Dasar Ke Lagu-Lagu Populer. ")
       elif pilih ==2:
              biaya_admin= biaya * 3/100
              silver= biaya + biaya_admin
              print(f"Untuk Harga Paket Silver Dan Biaya Administrasinya jadi:{silver}")
              print("Dengan Keuntungan Akses Lagu Premium Dan Playlist Kustom. ")
       elif pilih ==3:
             biaya_admin= biaya * 5/100
             gold= biaya + biaya_admin
             print(f"Untuk Harga Paket Gold Dan Biaya Administrasinya jadi:{gold}")
             print("Dengan Keuntungan Akses Lagu Premium, Playlist Kustom, Dan Mode Offline. ")
       elif pilih ==4:
              biaya_admin= biaya * 7/100
              platinum= biaya + biaya_admin
              print(f"Untuk Harga Paket Platinum Dan Biaya Administrasinya jadi:{platinum}")
              print("Dengan Keuntungan Akses Semua Fitur, Playlist Kustom, Mode Offline, Dan Konten Eksklusif Artis.")
       else:
            print("Opsi Yang Anda Pilih Tidak ada")
              
              


else:
    print("Login Gagal Coba lagi")