from variabel import pengguna, pemain 
from pemain import tampilkan_data_pemain, tambah_pemain_baru, hapus_pemain, update_harga_pemain
from menulogin import tampilkan_menu_login

while True:
    tampilkan_menu_login()
    try:
        pilih = int(input("Pilih menu: "))
    except ValueError:
        print("Input harus berupa angka!")
        continue

    if pilih == 1:
        print("REGISTRASI AKUN BARU")
        user = input("MASUKAN NAMA ANDA: ")
        password = input("MASUKAN PASSWORD: ")
        while True:
            role = input("MASUKAN ROLE ANDA (pengguna/admin): ").lower()
            if role in ["admin", "pengguna"]:
                break
            else:
                print("Role tidak valid.")
        if user in pengguna:
            print("User Sudah Ada Yang Pake Coba Lagi Yang lain")  
        else:
            pengguna[user] = {"password": password, "role": role}
            print("Registrasi berhasil!")

    elif pilih == 2:
        if len(pengguna) == 0:
            print("Belum ada akun yang terdaftar. Silakan registrasi terlebih dahulu.")
        else:
            print("==========MENU LOGIN==========")
            akun_login = input("MASUKAN NAMA: ")
            akun_pw = input("MASUKAN PASSWORD: ")
            role = input("Masukan Role (pengguna/admin): ").lower()

            if akun_login in pengguna and pengguna[akun_login]["password"] == akun_pw and pengguna[akun_login]["role"] == role:
                if role == "admin":
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
                        try:
                            menu = int(input("MASUKAN PILIHAN SALAH SATU DI MENU ADMIN:"))
                        except ValueError:
                            print("Input harus berupa angka!")
                            continue
                        if menu == 1:
                            tambah_pemain_baru()
                        elif menu == 2:
                            tampilkan_data_pemain(pemain)
                            nama = input("Masukkan nama pemain: ")
                            try:
                                harga = int(input("Masukkan harga baru: "))
                                update_harga_pemain(nama, harga)
                            except ValueError:
                                print("Harga harus berupa angka!")
                        elif menu == 3:
                            tampilkan_data_pemain(pemain)
                            hapus_pemain()
                        elif menu == 4:
                            tampilkan_data_pemain(pemain)
                        elif menu == 5:
                            print("Keluar dari aplikasi.")
                            exit()
                        else:
                            print("Pilihan tidak valid Pilih 1 Sampai 5 Saja.")
                elif role == "pengguna":
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
                        try:
                            menu = int(input("Masukan Pilihan di Salah Satu Di Menu:")) 
                        except ValueError:
                            print("Input harus berupa angka!")
                            continue

                        if menu == 1:
                            tampilkan_data_pemain(pemain)
                        elif menu == 2:
                            tambah_pemain_baru()
                        elif menu == 3:
                            print("Keluar dari aplikasi.")
                            exit()
                        else:
                            print("Pilihan tidak valid Pilih 1 Sampai 3 Saja.")
            else:
                print("Login gagal. Periksa kembali nama, password, dan role Anda.")
    else:
        print("Pilihan tidak valid Pilih 1 Sampai 2 Saja.")