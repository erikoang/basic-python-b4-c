def my_function():
    print("Hello from a function")

my_function()

def another_function(name, umur="0"): #Parameternya bisa langsung di define disini, angggap saja sebagai default (name="Default")
#Default artinya parameter yang bisa tidak diisi karena sudah ada value dari awalnya
    print("hello", name, "yang berumur", umur, "tahun")

another_function("Koang", "18")
another_function("Koang")

#Parameter juga tidak perlu berurutan asalnya keywordnya di define dengan jelas saja
another_function(umur="15", name="Ellen")

#Function Return Value
print("-------------------------")
print("FUNCTION RETURN VALUE")
def my_function3(x):
    return 5 * x

#Konsepnya -> my_function(3) = 5*3 = 45

print(my_function3(3))

#kapan pake return dan print, biasanya kalo print kalo bentuknya text sedangkan kalo misalnya return kalo ada operasi matematika aga dikembalikan dulu baru bisa di cetak