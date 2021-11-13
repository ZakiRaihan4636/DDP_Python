# Nama Pelanggan
nama_pelanggan = input("Masukan Nama : ")

#Daftar Produk Toko Online
print("-------Toko Online-------")
print("Daftar Produk Elektronik")
print("1. Kipas Angin")
print("2. AC")
print("3. Mesin Cuci")
print("4. TV")
print("5. Kulkas")
print("-------------------------")
print("*Pilih produk menggunakan angka sesuai dengan nomor produk")

# input nama produk meggunakan angka atau integer sesuai dengan nomor produk
produk = int(input("Pilih produk : "))

# input jumlah beli
jumlah_beli = int(input("Jumlah Beli : "))

#If multi kondisi Harga produk
if(produk == 1):
    nama_produk = "Kipas Angin"
    harga = 1000000
elif(produk == 2):
    nama_produk = "AC"
    harga = 2000000
elif(produk == 3):
    nama_produk = "Mesin Cuci"
    harga = 3000000
elif(produk == 4):
    nama_produk =  "TV"
    harga = 4000000
elif(produk == 5):
    nama_produk = "Kulkas"
    harga = 5000000
else:
    nama_produk = "produk tidak ditemukan"
    harga = 0


# harga Kotor
harga_kotor = (harga * jumlah_beli)

# If multi kondisi Diskon produk
if(produk == 1 and jumlah_beli >= 5):
    diskon = 20/100
    harga_diskon = harga_kotor * 20/100
elif(produk == 2 and jumlah_beli >= 3):
    diskon = 10/100
    harga_diskon = harga_kotor * 10/100
else:
    diskon = 5/100
    harga_diskon = harga_kotor * 10/100


# PPN 10% di tanggung pembeli
ppn = (harga_kotor - harga_diskon) * 10/100

# Harga bersih
harga_bersih = (harga_kotor - harga_diskon) + ppn

# cetak
print("-------------------------")
print("Nama Pelanggan :",nama_pelanggan)
print("Produk Pilihan :",nama_produk)
print("Harga Produk   :",harga)
print("Jumlah Beli    :",jumlah_beli,"pcs")
print("Harga Kotor    :",harga_kotor)
print("Diskon         :",diskon)
print("PPN            :",ppn)
print("Harga Bersih   :",harga_bersih)
print("--------------------------")