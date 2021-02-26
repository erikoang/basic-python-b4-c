dictPelanggan1 = {
    "Nama" : "Udin",
    "Umur" : 18
}

dictPelanggan2 = {
    "Nama" : "Henry",
    "Umur" : 35
}

print(dictPelanggan1)

#Ambil Keys spesifik
print("Nama = {}".format(dictPelanggan1["Nama"]))

#Change Value
dictPelanggan1["Umur"] = 22
print("Umur setelah di change value = {}".format(dictPelanggan1["Umur"]))

#Loop through a dictionary
#for x in dictPelanggan1:
    #print(x) #Keysnya
    #print(dictPelanggan1[x]) #Valuesnya
    #print("---------------")
    #print(x,"=",dictPelanggan1[x]) #Kalo digabung

for x in dictPelanggan1.keys():
    print(x)

for x,y in dictPelanggan1.items():
    print("{}: {}".format(x,y))

#list of dictionary
print("-----------------------------------------------")
print("LIST OF DICTIONARY")
daftar_pelanggan = []
daftar_pelanggan.append(dictPelanggan1)
daftar_pelanggan.append(dictPelanggan2)

for pelanggan in daftar_pelanggan:
    print("Nama: {}".format(pelanggan["Nama"]))
    print("Umur: {}".format(pelanggan["Umur"]))