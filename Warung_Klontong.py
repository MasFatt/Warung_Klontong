print("========================= WARUNG SARAPAN PAGI =========================")
Pembeli = input("Nama Pembeli : ")

#menambahkan fungsi pada variable makanan. Fungsi di bawah, jika dipanggil, akan mengeksekusi perintah print() yang ada di dalamnya.
def makanan():
    global totalmakanan
    global porsi
    global makan
    print("\n========================= MENU MAKANAN =========================")
    print("1. Nasi Uduk - Rp.7000")
    print("2. Nasi Kuning - Rp.7000")
    print("3. Nasi Rames - Rp.10000")
    print("4. Nasi Telur - Rp.13000")
    print("5. Nasi Ayam - Rp.15000")
    nomor = int(input("Masukkan pilihan 1/2/3/4/5 : "))
    porsi = int(input("Berapa Porsi : "))


#Selanjutnya, kita juga terkadang akan membutuhkan fungsi IF...ELSE...ELIF. Elif merupakan singkatan dari else if. Fungsi Ini membuat kita diperkenankan memeriksa beberapa ekspresi. Jika kondisi if False, maka sistem akan langsung mengecek kondisi yang ada di elif berikutnya. Sementara jika semua kondisi elif salah, maka pernyataan else lah yang akan dieksekusi. Meskipun ada banyak kondisi, hanya satu kondisi di antara beberapa blok if...elif...else yang akan dieksekusi.
    if nomor == 1:
        totalmakanan = porsi * 7000
        print(porsi,' Nasi Uduk = Rp.',totalmakanan)
        makan=("Nasi Uduk")
    elif nomor == 2:
        totalmakanan = porsi * 7000
        print(porsi,' Nasi Kuning = Rp.',totalmakanan)
        makan=("Nasi Kuning")
    elif nomor == 3:
        totalmakanan = porsi * 10000
        print(porsi,' Nasi Rames = Rp.',totalmakanan)
        makan=("Nasi Rames")
    elif nomor == 4:
        totalmakanan = porsi * 13000
        print(porsi,' Nasi Telur = Rp.',totalmakanan)
        makan=("Nasi Telur")
    elif nomor == 5:
        totalmakanan = porsi * 15000
        print(porsi,' Nasi Ayam = Rp.',totalmakanan)
        makan=("Nasi Ayam")
    else:
        print("Pilihan tidak ada di daftar menu\nsilahkan pilih kembali !!!")
        makanan()
        
#menambahkan fungsi pada variable minuman. Fungsi di bawah, jika dipanggil, akan mengeksekusi perintah print() yang ada di dalamnya.
def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n========================= MENU MINUMAN =========================")
    print("1. Es Teh - Rp.3000")
    print("2. Es Nutrisari - Rp.3000")
    print("3. Kopi - Rp.5000,00")
    nomor = int(input("Masukkan pilihan 1/2/3 : "))
    gelas = int(input("Berapa gelas : "))

#Selain IF, kita juga akan sering menggunakan fungsi IF...ELSE, dimana jika kondisi salah, kita masih memiliki pilihan lain yang bisa dilakukan pengujian. Pernyataan IF...ELSE mengevaluasi ekspresi pengujian dan akan mengeksekusi isi if hanya jika kondisi pengujian adalah True. Sementara jika kondisinya False, body dari else yang akan dieksekusi. Indentation di dalam fungsi ini akan digunakan untuk memisahkan blok yang ada.
    if nomor == 1:
        totalminuman = gelas * 3000
        print(gelas,' Es Teh = Rp.',totalminuman)
        minum=("Nasi Uduk")
    elif nomor == 2:
        totalminuman = porsi * 3000
        print(gelas,' Es Nutrisari = Rp.',totalminuman)
        minum=("Es Nutrisari")
    elif nomor == 3:
        totalminuman = porsi * 5000
        print(gelas,' Kopi = Rp.',totalminuman)
        minum=("Kopi")
    else:
        print("Pilihan tidak ada di daftar menu\nsilahkan pilih kembali !!!")
        minuman()

#Rumus penjumlahan dari sub total = totalmakanan + totalminuman
makanan()
minuman()
total_semua = totalmakanan + totalminuman

print("\nTotal yang harus di bayar : Rp.",total_semua)
uang = int(input("Uang Tunai Pembeli : Rp."))
kembalian = int(uang - total_semua)
print("kembalian :", kembalian)

print("\n========================= S T R U K B E L I =====================")
print("Nama\t\t:",Pembeli)
print("Beli\t\t:",porsi,makan,"(Rp.",totalmakanan,")")
print("Beli\t\t:",gelas,minum,"(Rp.",totalminuman,")")
print("Tagihan\t\t:Rp.",total_semua)
print("Dibayar\t\t:Rp.",uang)
print("Kembalian\t:Rp.",kembalian)

print("===================================================================")
