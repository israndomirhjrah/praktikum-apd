pengguna={}
pemain = {
    "lamine yamal": 100000,
    "lewandowski": 50000,
    "raphinha": 80000
}

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
        
          
        akunterdaftar = user in pengguna
          
        if akunterdaftar:
             print("User Sudah Ada Yang Pake Coba Lagi Yang lain")    
        else:  
             pengguna[user]={"password":password,"role":role}
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
                 pemain.update({tambah_pemain : tambah_harga})
                 angka=1
                 for i, j in  pemain.items():
                    print(f"{angka}. {i} - euro{j} - club:{club}")
                    angka +=1
               elif pilih == 2:
                 print("=======Menu Update Harga Pemain======")
                 angka=1
                 for i, j in  pemain.items():
                    print(f"{angka}. {i} - euro{j} - club:{club}")
                    angka +=1
                 idx = input("Masukkan nama pemain: ")
                 harga_baru = int(input("Masukkan harga baru: "))
                 pemain[idx] = harga_baru
                 angka=1
                 for i, j in  pemain.items():
                    print(f"{angka}. {i} - euro{j} - club:{club}")
                    angka +=1
               elif pilih == 3:
                  print("=======Menu Hapus Pemain======")
                  angka=1
                  for i, j in  pemain.items():
                    print(f"{angka}. {i} - euro{j} - club:{club}")
                    angka +=1
                  hapus_pemain=(input("Masukan Pemain:"))
                  del pemain [hapus_pemain]
                  angka=1
                  for i, j in  pemain.items():
                    print(f"{angka}. {i} - euro{j} - club:{club}")
                    angka +=1
               elif pilih == 4:
                  print("========DATA PEMAIN=======")
                  angka=1
                  for i, j in  pemain.items():
                    print(f"{angka}. {i} - euro{j} - club:{club}")
                    angka +=1
               elif pilih == 5:
                  print("Anda Tekeluar Dari Aplikasi")
                  exit()
               else:
                 print("Pilihan tidak valid Pilih 1 Sampai 5 Saja.")
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
                  angka=1
                  for i, j in  pemain.items():
                    print(f"{angka}. {i} - euro{j} - club:{club}")
                    angka +=1

                elif pilih == 2:
                 print("=======Menu Menambahkan Pemain=======")
                 tambah_pemain=input("Tambahkan Pemain:")
                 tambah_harga=int(input("Masukan Harga Beli:"))
                 pemain.update({tambah_pemain : tambah_harga})
                 angka=1
                 for i, j in  pemain.items():
                    print(f"{angka}. {i} - euro{j} - club:{club}")
                    angka +=1
                elif pilih == 3:
                   print("Anda Keluar program")
                   exit()
                else:
                 print("Pilihan tidak valid Pilih 1 Sampai 3 Saja.")
            else:
             print("login Gagal.")
    else:
      print("Pilihan tidak valid Pilih 1 Sampai 2 Saja.")
       
