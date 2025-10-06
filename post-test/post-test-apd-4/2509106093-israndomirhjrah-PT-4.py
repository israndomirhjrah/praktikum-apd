nama_user="israndomirhjrah"
nim_password=2509106093
total=0
percobaan=0

while percobaan <3:

         nama=input("Masukan Nama:")
         nim=int(input("Masukan Nim:"))
 
         if nama == nama_user and nim == nim_password:
          while True:
           print("Login Berhasil")  
           print("=====Menu Pembelian Ticket====")
           print("1.Tiket Reguler dengan Harga per tiket Rp 50.000")
           print("2.Tiket VIP dengan Harga per tiket Rp.100.000")
           print("3.Tiket VVIP dengan Harga per tiket Rp.150.000")
           print("4.Keluar Dari Aplikasi")
           print("")
           print("====Promo====")
           print("")
           print("Jika Pembelian Sampai Rp.300.000 Mendapatkan Diskon 12%")
           print("Jika Pembelian Sampai Rp.200.000 Mendapatkan Diskon 8%")
           print("Jika Pembelian Sampai Rp.150.000 Maka Mendapatkan Poster Ekslusif")
           
    
           pilih=int(input("Pilih Ticket Yang Mau Di Beli:"))
           if pilih == 1:
            harga=50000
            jenisticket="Reguler"
           elif pilih == 2:
            harga=100000
            jenisticket="VIP"
           elif pilih == 3:
            harga=150000
            jenisticket="VVIP"
        
           else:
            print("Anda Tekeluar Dari Program")  
            break
           jumlahticket=int(input(f"Masukan Berapa Ticket{jenisticket} Yang Mau Di Pesan:"))

           for i in range (jumlahticket):
            total += harga
          
   
           if total >=300000:
             diskon=total * 12/100
             bayar=total-diskon
             print("====Rician Struk====")
             print(f"Jenis Tiket   : {jenisticket}")
             print(f"Jumlah Tiket  : {jumlahticket}")
             print(f"Total Bayar   : Rp{bayar}")
             print("Mendapatkan Diskon : 12%")
             print("")
             print("")
             
           elif total >=200000:
             diskon=total * 8/100
             bayar=total-diskon
             print("====Rician Struk====")
             print(f"Jenis Tiket   : {jenisticket}")
             print(f"Jumlah Tiket  : {jumlahticket}")
             print(f"Total Bayar   : Rp{bayar}")
             print("Mendapatkan Diskon : 8%")
             print("")
             print("")
                  
           elif total >=150000:
             print("====Rician Struk====")
             print(f"Jenis Tiket   : {jenisticket}")
             print(f"Jumlah Tiket  : {jumlahticket}")
             print(f"Total Bayar   : Rp{total}")
             print("Mendapatkan Poster Ekslusif ")
             print("")
             print("")
             
           else:
             print("====Rician Struk====")
             print(f"Jenis Tiket   : {jenisticket}")
             print(f"Jumlah Tiket  : {jumlahticket}")
             print(f"Total Bayar   : Rp{total}")
             print("Mendapatkan Diskon : Tidak ")
             print("")
             print("")
             
         else:
          print("Nama Dan Nim Anda Masukan Salah Coba Lagi")
          percobaan +=1

else:
    print("Percobaan login habis. Akses ditolak.")

