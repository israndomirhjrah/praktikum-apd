nama=input("MASUKAN NAMA ANDA:")
nim=int(input("MASUKAN NIM ANDA:"))

print("") #JARAK
print("ADA LAPTOP ACER")
print("ADA LAPTOP ASUS")
print("ADA LAPTOP LENOVO ")
print("") #JARAK
print("ADA DISKON AKHIR BULAN")
print("") #JARAK
print("UNTUK LAPTOP ACER DISKON 5%")
print("UNTUK LAPTOP ASUS DISKON 7%")
print("UNTUK LAPTOP LENOVO DISKON 10%")
print("") #JARAK

harga=int(input(f"{nama} DENGAN NIM:{nim} INGIN MEMBELI LAPTOP SEHARGA:"))

diskon = harga * 5/100
acer= harga-diskon

diskon = harga * 7/100
asus= harga-diskon

diskon = harga * 10/100
lenovo= harga-diskon
print("") #JARAK
print(f"Jika {nama} membeli laptop Acer ia harus membayar {acer} setelah mendapat diskon 5%")
print(f"Jika {nama} membeli laptop ASUS ia harus membayar {asus} setelah mendapat diskon 7%")
print(f"Jika {nama} membeli laptop LENOVO ia harus membayar {lenovo} setelah mendapat diskon 10%")
