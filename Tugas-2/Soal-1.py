daftarKontak = []

def printDaftarKontak():
    for kontak in daftarKontak:
        print("Nama: ", kontak["Nama"])
        print("No. Telepon", kontak["No. Telepon"])
        print("-------------------")
    

def tambah(namaPemilikKontak, nomorPemilikKontak):
    daftarKontak.append({"Nama" : namaPemilikKontak, "No. Telepon" : nomorPemilikKontak})

while True:
    print("Selamat Datang!")
    print("-----Menu------")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    menuPilihan = int(input("Pilih menu: "))
    if menuPilihan == 1:
        if len(daftarKontak) > 0:
            printDaftarKontak()
        else:
            print("Tidak ada kontak yang terdaftar")
        continue
    elif menuPilihan == 2:
        namaPemilikKontak = input("Nama: ")
        nomorPemilikKontak = input("Nomor: ")
        tambah(namaPemilikKontak, nomorPemilikKontak)
        print("Kontak berhasil ditambahkan")
        continue
    elif menuPilihan == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")
        continue