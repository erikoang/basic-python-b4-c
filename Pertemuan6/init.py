class Person:
    #constructor 
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

#Membuat berdasarkan constructor
p2 = person("Nafi",22)
p1 = person("Alex",15)

print("Nama orang pertama :", p1.nama)
print("Umur orang pertama :", p1.umur)
print("Nama orang kedua :", p2.nama)
print("Umur orang kedua :", p2.umur)