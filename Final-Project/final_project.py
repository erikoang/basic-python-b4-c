import smtplib, ssl
from getpass import getpass #https://www.youtube.com/watch?v=hk3ubc1-ZGg

def siapinListEmail(): #https://www.kite.com/python/answers/how-to-replace-a-string-in-a-list-in-python
    f = open("receiver_list.txt", "r")
    for x in f:
        email = x.replace("\n", "")
        kumpulan_email.append(email)
    f.close()

def tampilinEmail():
    if len(kumpulan_email) > 0:
        for x in kumpulan_email:
            print(x)
    else:
        print("Tidak ada email yang terdaftar")

def tambahListEmail():
    f = open("receiver_list.txt", "a")
    email_tambahan = input("Masukkan Email yang ingin ditambah: ")
    f.write(email_tambahan+"\n")
    f.close()

def kirimPesan(): # https://realpython.com/python-send-email/
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "nemeror@gmail.com"
    password = getpass("Type your password and press enter:")
    message = """Subject: Hello Guys\n\nThis is a mail that sent from python"""

    for x in kumpulan_email:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, x, message)

while True:
    kumpulan_email = []
    siapinListEmail()
    print("Selamat Datang!")
    print("-----Menu------")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Kirim Pesan")
    print("4. Keluar dari Program")
    menuPilihan = int(input("Pilih menu: "))
    if menuPilihan == 1:
        tampilinEmail()
        continue
    elif menuPilihan == 2:
        tambahListEmail()
        continue
    elif menuPilihan == 3:
        kirimPesan()
        continue
    elif menuPilihan == 4:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")
        continue