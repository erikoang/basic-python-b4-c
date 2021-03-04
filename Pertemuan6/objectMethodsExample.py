class Person:
    #constructor 
    def __init__(self, nama, umur, tempatLahir, tanggalLahir, status):
        self.nama = nama
        self.umur = umur
        self.tempatLahir = tempatLahir
        self.tanggalLahir = tanggalLahir
        self.status = status

    #method / function
    def myFunc(self):
        print("Orang ini bernama", self.nama, "dengan usia", self.umur ,"tahun. Beliau lahir di", self.tempatLahir ,"pada", self.tanggalLahir,"dan sekarang statusya", self.status)


nama = input("Masukkan nama anda: ")
umur = input("Masukkan umur anda: ")
tempatLahir = input("Dimanakah anda lahir: ")
tanggalLahir = input("Kapan anda lahir: ")
status = input("Status anda terkini adalah: ")

p1 = Person(nama, umur, tempatLahir, tanggalLahir, status)
p1.myFunc()