class Person:
    #constructor 
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    #method / function
    def myFunc(self):
        print("Hello my name is", self.nama,"and I am",self.umur)

p1 = Person("John", 36)
p1.myFunc()