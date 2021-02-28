while True:
    print("Selamat Datang!")
    print("-----Menu------")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    menuPilihan = int(input("Pilih menu: "))
    if menuPilihan == 1:
        f = open("file.txt", "r")
        print(f.read())
    elif menuPilihan == 2:
        namaPemilikKontak = input("Nama: ")
        nomorPemilikKontak = input("Nomor: ")
        f = open("file.txt", "a")
        f.write("----------------\n")
        f.write(namaPemilikKontak + "\n")
        f.write(nomorPemilikKontak + "\n")
        f.close()
        print("Kontak berhasil ditambahkan")
        continue
    elif menuPilihan == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")
        continue

#buat hapus
#clear = open("file.txt","w")
#clear.close