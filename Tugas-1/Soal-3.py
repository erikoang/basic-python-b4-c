nilaiPraktek = int(input("Masukkan nilai ujian praktek: "))
nilaiTeori = int(input("Masukkan nilai ujian teori: "))

if(nilaiPraktek >= 70 and nilaiTeori >= 70):
    print("Selamat, anda lulus!")
elif(nilaiTeori >= 70):
    print("Anda harus mengulang ujian praktek")
elif(nilaiPraktek >= 70):
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")