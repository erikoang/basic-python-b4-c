nilai = [100,70,50,80,30,60]

for i in nilai:
    if i <=50:
        continue
    print("Nilai mereka {} = lulus".format(i))

for i in range(6):
    if i == 1:
        continue
    elif i == 4:
        break
    print(i)