class person : #superclass
    #Constructor
    def __init__ (self, nama, umur):
        self.nama = nama
        self.umur = umur

    #method/function:
    def tampil(self):
        print(self.nama)
        print(self.umur)

class special_id(person): #subclass
    #Constructor
    def __init__ (self, nama, umur, alamat, status):
        self.alamat = alamat
        self.status = status
        #Penurunan Sifat/Data
        person.__init__(self,nama,umur)
    def tampil(self):
        print(self.nama)
        print(self.umur)
        print(self.alamat)
        print(self.status)

p1 = special_id("Nafi",22,"Malang","Mahasiswa")
p1.tampil()