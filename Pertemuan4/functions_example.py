nama_buah = []

def print_nama_buah():
    for buah in nama_buah:
        print(buah)
    print("============")

def tambah(nama):
    nama_buah.append(nama)
    print_nama_buah()

tambah("apel")
tambah("jeruk")
tambah("melon")