#Append to File
#f = open("file.txt", "a")
#a = input("Masukkan nama : ")
#f.write(a)
#f.close()

#Write to File
#f = open("file.txt", "w")
#a = input("Masukkan nama : ")
#f.write(a)
#f.close()

#Read to File
#f = open("file.txt", "r")
#print(f.read())
#print(f.readline()) #untuk print perbaris
#f.close()

#Delete File txt
import os
#os.remove("file.txt")

#Current Directory
p = os.getcwd()
print(p)
#Make Directory
#os.mkdir("D:\MyPythonProject")