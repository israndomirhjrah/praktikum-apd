pengguna=[]
pemain = [
    ["lamine yamal", 100000],
    ["lewandowski", 50000],
    ["raphinha", 80000]
]

club= "barcelona"
 
while True:
    print("""
=================================================
|                                               |
|                                               |
|   Selamat Datang di Aplikasi Barcelona Bola   |
|               MENU LOGIN                      |
|                                               |
|    1. REGISTRASI AKUN BARU                    |
|    2. LOGIN SUDAH PUNYA AKUN                  |
|                                               |
=================================================
 """)  #register akun
    pilih=int(input("Pilih yang ada di Menu login:"))
    if pilih == 1:
        print("REGISTRASI AKUN BARU")
        user=input("MASUKAN NAMA ANDA:")
        password=input("MASUKAN PASSWORD YANG ANDA INGINKAN:")

        while True:
            role = input("MASUKAN ROLE ANDA PENGGUNA/ADMIN: ")
            if role == "admin" or role == "pengguna":
                break
            else:
                print("role tidak ada. Silakan masukkan 'admin' atau 'pengguna'.")
        
        akunterdaftar = False
        for data_akun in pengguna:
         if data_akun[0]== user: 
          akunterdaftar = True
          
        if akunterdaftar:
             print("User Sudah Ada Yang Pake Coba Lagi Yang lain")    
        else:  
             pengguna.append([user, password, role])
             print("Registrasi berhasil!")
          
         
    
    elif pilih == 2:
           while True:
            print("==========LOGIN==========")
            akun_login=input("MASUKAN NAMA ANDA YANG SUDAH DIBUAT:")
            akun_pw=input("MASUKAN PASSWORD ANDA YANG SUDAH DIBUAT:")
            role=input("Masukan Role anda Pengguna/Admin:")
            if akun_login == user and akun_pw == password and role == "admin":
              while True:
               print("""
=================================================
|                                               |
|                                               |
|   Selamat Datang di Aplikasi Barcelona Bola   |
|                 MENU ADMIN                    |
|                                               |
|     1. Menambahkan Pemain Baru/Pinjaman       |
|     2. Update Harga Pemain                    |
|     3. Hapus Pemain                           |
|     4. Tampilkan Pemain                       |
|     5. keluar                                 |
=================================================""")
               pilih=int(input("MASUKAN PILIHAN SALAH SATU DI MENU ADMIN:"))
               if pilih == 1:
                 print("=======Menu Menambahkan Pemain=======")
                 tambah_pemain=input("Tambahkan Pemain:")
                 tambah_harga=int(input("Masukan Harga Beli:"))
                 pemain.append([tambah_pemain,tambah_harga])
                 print(pemain)
               elif pilih == 2:
                 print("=======Menu Update Harga Pemain======")
                 for i in range(len(pemain)):
                  print(pemain)
                  idx = int(input("Masukkan urutan ke berapa harga pemain yang ingin diubah: "))
                  harga_baru = int(input("Masukkan harga baru: "))
                  pemain[idx][1] = harga_baru
                  print(pemain)
               elif pilih == 3:
                 print("=======Menu Hapus Pemain======")
                 print(pemain)
                 for i in range(len(pemain)):
                  hapus_pemain=int(input("Masukan Urutan Pemain:"))
                  del pemain [hapus_pemain]
                  print(pemain)
               elif pilih == 4:
                  print("========DATA PEMAIN=======")
                  for i in range(len(pemain)):
                   print(f"{i+1}. {pemain[i][0]} - euro{pemain[i][1]} - club:{club}")
               else:
                  print("Anda Tekeluar Dari Aplikasi")
                  exit()
            elif akun_login == user and akun_pw == password and role == "pengguna":
               while True:
                print("""
=================================================
|                                               |
|                                               |
|   Selamat Datang di Aplikasi Barcelona Bola   |
|                 MENU PENGGUNA                 |
|                                               |
|     1. Tampilkan pemain                       |
|     2. Menambahkan Pemain Baru/Pinjaman       |
|     3. Keluar                                 |
|                                               |
|                                               |
=================================================
""")            
                pilih=int(input("Masukan Pilihan di Salah Satu Di Menu:")) 
                if pilih == 1:
                  print("========DATA PEMAIN=======")
                  for i in range(len(pemain)):
                   print(f"{i+1}. {pemain[i][0]} - euro{pemain[i][1]} - club:{club}")

                elif pilih == 2:
                    print("=======Menu Menambahkan Pemain=======")
                    tambah_pemain=input("Tambahkan Pemain:")
                    tambah_harga=int(input("Masukan Harga Beli:"))
                    pemain.append([tambah_pemain,tambah_harga])
                    print(pemain)
                elif pilih == 3:
                   print("Anda Keluar program")
                   exit()
                else:
                 print("Pilihan tidak valid.")
    else:
       print("Pilihan tidak valid.")
