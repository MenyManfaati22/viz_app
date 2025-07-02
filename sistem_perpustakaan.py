buku = []

# Fungsi untuk menampilkan semua data
def tampilkan_buku():
    print("\n")
    print("----------- Daftar Buku ----------")
    # Check jika jumlah value pada variable buku
    # Jika =0 print("Belum Ada Data")
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    # Jika jumlah lebih dari 0, maka kita print buku satu persatu beserta indexnya
    # menggunakan For loops
    else:
        for index in range(len(buku)):
            print("["+str(index)+"]", str(buku[index]))

# fungsi untuk menambah data
def masukkan_data_buku():
    # Supaya interaktif, kita buat user input dengan menggunakan fungsi input()
    buku_baru = input("Masukkan Judul Buku: ")
    # gunakan method .append() untuk menambah nilai baru
    # perlu diingat method .append() berbeda dengan konsep extending list yang menggunakan (+) *) List + List
    buku.append(buku_baru)
    print("Buku dengan judul: \"" + buku_baru + "\" telah berhasil dimasukkan")
# fungsi untuk edit data
def edit_data_buku():
    # Tampilkan data buku dengan memanggil fungsi tampilkan_buku
    tampilkan_buku()
    # Buat user input untuk memasukkan ID buku yang akan di edit
    index = input("Inputkan ID buku yang akan di edit: ")
    index = int(index)
    # Check jika ID yang dimasukkan lebih besar dari jumlah buku, maka print("ID Salah")
    if(index + 1 > len(buku)):
        print("ID salah")
    # Else, replace list element dengan judul_baru
    else:
        judul_baru = input("Judul baru: ")
        buku[index] = judul_baru
        print("Buku dengan judul baru: \"" + judul_baru + "\" telah berhasil diubah")
# fungsi untuk menhapus data
def hapus_data_buku():
    tampilkan_buku() #Tampilkan data buku
    index = input("Inputkan ID buku yang akan di hapus: ") #gunakan input() untuk mendapatkan ID dari user input
    index = int(index)
    # Check jika ID yang dimasukkan lebih besar dari jumlah buku, maka print("ID Salah")
    if(index + 1 > len(buku)):
        print("ID salah")
    # Else, remove data buku menggunakan method .remove(buku[index]) atau del(buku[index])
    else:
        buku.remove(buku[index])
        print("Buku dengan index: \"" + str(index) + "\" telah berhasil dihapus")
def tampilkan_menu_utama():
    print("\n")
    print("----------- SISTEM PERPUSTAKAAN ----------")
    print("[1] Tampilkan Buku")
    print("[2] Masukkan Data Buku")
    print("[3] Edit Data Buku")
    print("[4] Hapus Data Buku")
    print("[5] Exit")
    
    # Buat input user menggunakan fungsi input()
    # kemudian, buat control flow yang bisa memanage pilihan input
    
    menu = input("PILIH MENU> ")
    print("\n")

    if menu == "1":
        tampilkan_buku()
    elif menu == "2":
        masukkan_data_buku()
    elif menu == "3":
        edit_data_buku()
    elif menu == "4":
        hapus_data_buku()
    elif menu == "5":
        exit()
    else:
        print("Salah pilih!")
if __name__ == "__main__":  

    while(True):
        tampilkan_menu_utama()