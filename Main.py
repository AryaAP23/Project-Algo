import os
import csv
import pandas as pd
from datetime import datetime

def clear():
    """Clear terminal"""
    os.system('cls')
    print("="*40)

def login():
    """Login Admin/User"""
    List=[]
    if os.path.exists("akun users.csv"):
        with open("akun users.csv", "r") as cek:
            lihat=csv.DictReader(cek)
            for row in lihat:
                List.append(row)
    ulang= 1
    while ulang == 1:
        clear()
        print(f"{'Login'.center(40)}\n{'='*40}")
        dataUser=[]
        username=input("Masukkan username >")
        pw=input("masukkan password >")
        if username == "admin" and pw == "2073":
            menuAdmin()
        for row in List:
            if row['Username'] == username and row['Password'] == pw:
                ulang=0
                dataUser.append(username)
                menu(dataUser)
        ulang=2
        while ulang == 2:
            ulang=0
            clear()
            print(f"{'Login'.center(40)}\n{'='*40}\n{'Akun tidak ditemukan'.center(40)}")
            tunggu=input("Tekan enter untuk mengulang/ketik (kembali) untuk kembali ke menu awal >")
            if tunggu =="":
                ulang=1
            elif tunggu == "kembali":
                pilihan_login()
            else:
                ulang=2

def daftar():
    """Daftar akun user"""
    List=[]
    if os.path.exists("akun users.csv"):
        with open("akun users.csv", "r") as cek:
            lihat=csv.DictReader(cek)
            for row in lihat:
                List.append(row)
    clear()
    print(f"{'Daftar'.center(40)}\n{'='*40}")
    x=1
    while x==1:
        x=0
        username=input("Username >")
        if username == "":
            x=1
    for i in List:
        if i['Username'] == username:
            b=1
            while b==1:
                b=0
                inputan = input("Username sudah ada. Tekan enter untuk mencoba lagi...")
                if inputan=="":
                    daftar()
                else:
                    b=1
    x=1
    while x==1:
        x=0
        pw=input("Password >")
        if pw == "":
            x=1
    confirm=input("Konfirmasi pasword >")
    if pw != confirm:
        clear()
        print(f"{'Daftar'.center(40)}\n{'='*40}")
        print(f"{'Pasword salah'.center(40)}\n>1. Ulang\n>0. Kembali")
        confirm=input("Pilihan >")
        if confirm == "1":
            daftar()
        elif confirm == "2":
            pilihan_login()
    clear()
    print(f"{'Daftar'.center(40)}\n{'='*40}\n{'Akun berhasil dibuat'.center(40)}")
    if not os.path.exists("akun users.csv"):
        Top  = ['Username','Password']
        with open("akun users.csv", "w") as make:
            buat = csv.writer(make)
            buat.writerow(Top)
    with open("akun users.csv", "a") as daftar2:
        top = ['Username', 'Password']
        masukkan = csv.DictWriter(daftar2, fieldnames=top)
        masukkan.writerow({'Username': username, 'Password': pw})
    while True:
        tunggu=input("Tekan enter untuk kembali")
        if tunggu=="":
            pilihan_login()

# ADMIN======================================================================================================================================
def menuAdmin():
    """Pilihan menu admin"""
    clear()
    print(f"{'Menu Admin'.center(40)}\n{'='*40}")
    print(f">1. Gudang\n>2. Katalog\n>3. Data Konsultasi\n>4. Data transaksi\n>5. Data masukan\n>0. Keluar\n{'='*40}")
    while True:
        pilihan = input("Pilihan >")
        if pilihan == "1":
            stokAdmin()
        elif pilihan == "2":
            katalogAdmin()
        elif pilihan == "3":
            konsultasiAdmin()
        elif pilihan == "4":
            dataTransaksi()
        elif pilihan == "5":
            dataMasukan()
        elif pilihan == "0":
            pilihan_login()

def stokAdmin():
    """Menampilkan data gudang dan tampilan menu Gudang"""
    clear()
    print(f"{'Gudang'.center(40)}\n{'='*40}")
    if not os.path.exists("gudang.csv"):
        print(f"{'Tidak ada stok'.center(40)}\n{'='*40}")
    else:
        List = []
        with open("gudang.csv", "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                List.append(row)
        data = pd.DataFrame(List)
        print(data)
    print(f"{'='*40}\n>1. Tambah stok\n>2. Hapus stok\n>3. Update stok\n>0. Kembali")
    while True:
        pilihan = input("Pilihan >")
        if pilihan == "1":
            tambahStok()
        elif pilihan == "2":
            hapusStok()
        elif pilihan == "3":
            updateStok()
        elif pilihan == "0":
            menuAdmin()

def tambahStok():
    """Tambah data dalam 'gudang.csv'"""
    clear()
    print(f"{'Tambah Stok'.center(40)}\n{'='*40}")
    List = []
    nama = input("Masukkan nama barang >")
    a=1
    while a==1:
        a=0
        jumlah = input("Masukkan jumlah barang >")
        if jumlah.isdigit():
            jumlah=int(jumlah)
        else:
            b=1
            while b==1:
                b=0
                inputan=input("Inputan salah. Tekan enter untuk mengulang")
                if inputan == "":
                    a=1
                else:
                    b=1
    a=1
    while a==1:
        a=0
        harga = input("Masukkan harga >")
        if harga.isdigit():
            harga=int(jumlah)
        else:
            b=1
            while b==1:
                b=0
                inputan=input("Inputan salah. Tekan enter untuk mengulang")
                if inputan == "":
                    a=1
                else:
                    b=1
    if not os.path.exists("gudang.csv"):
        with open("gudang.csv", "a") as make:
            Top = ['Produk', 'Jumlah', 'Harga']
            csv.DictWriter(make, fieldnames=Top)
    else:
        with open("gudang.csv", "r") as cek:
            lihat = csv.DictReader(cek)
            for row in lihat:
                List.append(row)
    for row in List:
        if row['Produk'] == nama:
            clear()
            print(f"{'Tambah Stok'.center(40)}\n{'='*40}\n{'Barang sudah ada'.center(40)}")
            print(f">1. Tambah stok lain\n>0. Kembali\n{'='*40}")
            while True:
                tunggu = input("Pilihan >")
                if tunggu == "1":
                    tambahStok()
                elif tunggu == "0":
                    stokAdmin()
    List.append({'Produk': nama, 'Jumlah': jumlah, 'Harga': harga})
    with open("gudang.csv", "w") as add:
        Top = ['Produk', 'Jumlah', 'Harga']
        tambah = csv.DictWriter(add, fieldnames=Top)
        tambah.writeheader()
        for new in List:
            tambah.writerow({'Produk':new['Produk'], 'Jumlah':new['Jumlah'], 'Harga':new['Harga']})
    clear()
    print(f"{'Tambah Stok'.center(40)}\n{'='*40}\n{'Barang berhasil dimasukkan'.center(40)}")
    print(f">1. Tambah stok\n>0. Kembali\n{'='*40}")
    while True:
        tunggu = input("Pilihan >")
        if tunggu == "1":
            tambahStok()
        elif tunggu == "0":
            stokAdmin()

def updateStok():
    """Update data dalam 'gudang.csv'"""
    List = []
    count=0
    if not os.path.exists("gudang.csv"):
        while True:
            inputan = input("Tidak ada stok. Tekan enter untuk kembali...")
            if inputan == "":
                stokAdmin()
    else:
        with open("gudang.csv", "r") as cek: #read
            lihat = csv.DictReader(cek)
            for row in lihat:
                List.append(row)
                count+=1
    data = pd.DataFrame(List)
    clear()
    print(f"{'Update Stok'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    b=1
    while b==1:
        b=0
        barang = input("Pilih nomer barang yang ingin diganti >")
        if barang.isdigit():
            barang=int(barang)
            if barang > count-1:
                c=1
                while c==1:
                    c=0
                    inputan=input("Inputan tidak valid. Tekan enter untuk mengulang...")
                    if inputan == "":
                        b=1
                    else:
                        c=1
        else:
            f=1
            while f==1:
                f=0
                inputan=input("Inputan tidak valid. Tekan enter untuk mengulang")
                if inputan == "":
                    b=1
                else:
                    f=1
    d=1
    while d==1:
        jenis = input("jenis yang ingin diganti >")
        if jenis == "Produk" or jenis == "Jumlah" or jenis == "Harga":
            d=0
        else:
            e=1
            while e==1:
                e=0
                inputan=input("Inputan tidak valid. Tekan enter untuk mengulang...")
                if inputan == "":
                    d=1
                else:
                    e=1
    a=1
    while a == 1:
        a=0
        baru = input("Data yang baru >")
        if baru == "":
            b=1
            while b==1:
                b=0
                inputan= input("Inputan tidak valid. Tekan enter untuk mengulang...")
                if inputan == "":
                    a=1
                else:
                    b=1
    data.loc[barang,jenis] = baru
    dicti = data.to_dict(orient='records')
    with open("gudang.csv", "w") as news:
        Top = ['Produk', 'Jumlah', 'Harga']
        tambah = csv.DictWriter(news, fieldnames=Top)
        tambah.writeheader()
        for new in dicti:
            tambah.writerow({'Produk':new['Produk'], 'Jumlah':new['Jumlah'], 'Harga':new['Harga']})
    clear()
    print(f"{'Update Stok'.center(40)}\n{'='*40}\n{data}\n{'='*40}\n{'Berhasil diubah'.center(40)}\n>1. Mengubah barang lagi\n>0. Kembali\n{'='*40}")
    while True:
        inputan = input("Pilihan >")
        if inputan == "1":
            updateStok()
        elif inputan == "0":
            stokAdmin()

def hapusStok():
    """Tambah data dalam 'gudang.csv'"""
    List = []
    listindex=[]
    count= 0
    if not os.path.exists("gudang.csv"):
        while True:
            inputan = input("Tidak ada stok. Tekan enter untuk kembali...")
            if inputan == "":
                stokAdmin()
    else:
        with open("gudang.csv", "r") as cek:
            lihat = csv.DictReader(cek)
            for row in lihat:
                List.append(row)
                listindex.append(count)
                count += 1
    del listindex[count-1]
    data = pd.DataFrame(List)
    clear()
    print(f"{'Hapus Stok'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    a=1
    while a==1:
        a=0
        inputan = input("Nomer barang yang ingin dihapus >")
        if inputan.isdigit():
            inputan=int(inputan)
            if inputan > count-1:
                c=1
                while c==1:
                    c=0
                    inputan=input("Inputan tidak valid. Tekan enter untuk mengulang...")
                    if inputan == "":
                        a=1
                    else:
                        c=1
        else:
            b=1
            while b==1:
                b=0
                inputan=input("Inputan tidak valid. Tekan enter untuk mengulang")
                if inputan == "":
                    a=1
                else:
                    b=1
    data = data.drop(inputan)
    data.index = listindex
    dicti = data.to_dict(orient='records')
    with open("gudang.csv", "w") as news:
        Top = ['Produk', 'Jumlah', 'Harga']
        tambah = csv.DictWriter(news, fieldnames=Top)
        tambah.writeheader()
        for new in dicti:
            tambah.writerow({'Produk':new['Produk'], 'Jumlah':new['Jumlah'], 'Harga':new['Harga']})
    clear()
    print(f"{'Hapus Stok'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    print(f">1. Menghapus lagi\n>0. Kembali\n{'='*40}")
    while True:
        inputan = input("Pilihan >")
        if inputan == "1":
            hapusStok()
        elif inputan == "0":
            stokAdmin()

def katalogAdmin():
    """Menu Data Katalog Admin"""
    clear()
    print(f"{'Katalog'.center(40)}\n{'='*40}")
    def tampilan(excel,logo):
        if not os.path.exists(excel):
            print(f"{'Tidak ada katalog'.center(40)}\n{'='*40}")
        else:
            print(f"{logo.center(40)}\n{'='*40}")
            listBibit = []
            with open(excel, "r") as see:
                lihat = csv.DictReader(see)
                for row in lihat:
                    listBibit.append(row)
            dataBibit = pd.DataFrame(listBibit)
            print(f"{dataBibit.to_string(max_colwidth=None)}\n{'='*40}")
    tampilan("bibit.csv","Bibit")
    tampilan("pupuk.csv","Pupuk")
    tampilan("pestisida.csv","Pestisida")
    print(f">1. Tambah katalog\n>2. Hapus katalog\n>3. Update katalog\n>0. Kembali")
    pilihan = input("Pilihan >")
    if pilihan == "0":
        menuAdmin()
    pilihan2= input("Bibit/Pupuk/Pestisida >")
    if pilihan == "1":
        if pilihan2 == "Bibit":
            tambahKatalog("bibit.csv")
        elif pilihan2 == "Pupuk":
            tambahKatalog("Pupuk.csv")
        elif pilihan2 == "Pestisida":
            tambahKatalog("pestisida.csv")
        else:
            katalogAdmin()
    elif pilihan == "2":
        if pilihan2 == "Bibit":
            hapusKatalog("bibit.csv")
        elif pilihan2 == "Pupuk":
            hapusKatalog("Pupuk.csv")
        elif pilihan2 == "Pestisida":
            hapusKatalog("pestisida.csv")
        else:
            katalogAdmin()
    elif pilihan == "3":
        if pilihan2 == "Bibit":
            updateKatalog("bibit.csv")
        elif pilihan2 == "Pupuk":
            updateKatalog("Pupuk.csv")
        elif pilihan2 == "Pestisida":
            updateKatalog("pestisida.csv")
        else:
            katalogAdmin()
    else:
        katalogAdmin()

def tambahKatalog(excel):
    """Tambah data dalam csv yang ditentukan"""
    clear()
    print(f"{'Tambah Katalog'.center(40)}\n{'='*40}")
    List=[]
    if os.path.exists(excel):
        with open(excel, "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                List.append(row)
    x=0
    while x==0:
        x=1
        produk= input("Masukkan produk >")
        a=1
        while a==1:
            harga = input("Masukkan harga >")
            if harga.isdigit():
                a=0
            else:
                a=1
        for row in List:
            if row['Produk'] == produk:
                print(f"{'='*40}\n{'Produk sudah ada'.center(40)}\n>1. Tambah produk lain\n>0. Kembali\n{'='*40}")
                y=0
                while y==0:
                    y=1
                    inputan=input("Pilihan >")
                    if inputan == "1":
                        tambahKatalog(excel)
                    elif inputan == "0":
                        katalogAdmin()
                    else:
                        y=0
        List.append({'Produk': produk, 'Harga': harga})
    with open(excel, "w") as new:
        Top= ['Produk', 'Harga']
        tambah = csv.DictWriter(new, fieldnames=Top)
        tambah.writeheader()
        for i in List:
            tambah.writerow({'Produk': i['Produk'], 'Harga': i['Harga']})
    print(f"{'='*40}\n>1. Tambah Katalog lagi\n>0. Kembali\n{'='*40}")
    while True:
        inputan=input("Pilihan >")
        if inputan == "1":
            tambahKatalog(excel)
        elif inputan == "0":
            katalogAdmin()

def hapusKatalog(excel):
    """Hapus data dalam csv yang ditentukan"""
    List=[]
    listindex=[]
    count= 0
    if not os.path.exists(excel):
        while True:
            inputan = input("Tidak ada data. Tekan enter untuk kembali...")
            if inputan == "":
                katalogAdmin()
    else:
        with open(excel, "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                List.append(row)
                listindex.append(count)
                count+=1
    del listindex[count-1]
    data = pd.DataFrame(List)
    clear()
    print(f"{'Hapus Katalog'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    a=1
    while a==1:
        a=0
        barang = input("Nomer yang ingin dihapus >")
        if barang.isdigit():
            barang=int(barang)
            if barang > count-1:
                c=1
                while c==1:
                    c=0
                    inputan=input("Inputan tidak valid. Tekan enter untuk mengulang...")
                    if inputan == "":
                        a=1
                    else:
                        c=1
        else:
            b=1
            while b==1:
                b=0
                inputan=int(input("Inputan tidak valid. Tekan enter untuk mengulang..."))
                if inputan == "":
                    a=1
                else:
                    b=1
    data = data.drop(barang)
    data.index = listindex
    dicti = data.to_dict(orient='records')
    with open(excel, "w") as news:
        Top = ['Produk', 'Harga']
        tambah = csv.DictWriter(news, fieldnames=Top)
        tambah.writeheader()
        for new in dicti:
            tambah.writerow({'Produk': new['Produk'], 'Harga': new['Harga']})
    clear()
    print(f"{'Hapus Katalog'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    print(f">1. Hapus lagi\n>0. Kembali")
    while True:
        inputan = input("Pilihan >")
        if inputan == "1":
            hapusKatalog(excel)
        elif inputan == "0":
            katalogAdmin()

def updateKatalog(excel):
    """Update data dalam csv yang ditentukan"""
    List = []
    count=0
    if not os.path.exists(excel):
        while True:
            inputan = input("Tidak ada stok. Tekan enter untuk kembali...")
            if inputan == "":
                katalogAdmin()
    else:
        with open(excel, "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                List.append(row)
                count+=1
    data = pd.DataFrame(List)
    clear()
    print(f"{'Update Katalog'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    a=1
    while a==1:
        a=0
        barang = input("Pilih nomer barang yang ingin diganti >")
        if barang.isdigit():
            barang=int(barang)
            if barang > count-1:
                b=1
                while b==1:
                    b=0
                    inputan=input("Inputan tidak valid. Tekan enter untuk mengulang...")
                    if inputan == "":
                        a=1
                    else:
                        b=1
        else:
            c=1
            while c==1:
                c=0
                inputan=input("Inputan tidak valid. Tekan enter untuk mengulang")
                if inputan == "":
                    a=1
                else:
                    c=1
    d=1
    while d==1:
        jenis = input("jenis yang ingin diganti >")
        if jenis == "Produk" or jenis == "Harga":
            d=0
        else:
            e=1
            while e==1:
                e=0
                inputan=input("Inputan tidak valid. Tekan enter untuk mengulang...")
                if inputan == "":
                    d=1
                else:
                    e=1
    f=1
    while f == 1:
        f=0
        baru = input("Data yang baru >")
        if baru == "":
            g=1
            while g==1:
                g=0
                inputan= input("Inputan tidak valid. Tekan enter untuk mengulang...")
                if inputan == "":
                    f=1
                else:
                    g=1
    data.loc[barang,jenis] = baru
    clear()
    print(f"{'Update Katalog'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    dicti = data.to_dict(orient='records')
    with open(excel, "w") as news:
        Top = ['Produk', 'Harga']
        tambah = csv.DictWriter(news, fieldnames=Top)
        tambah.writeheader()
        for new in dicti:
            tambah.writerow({'Produk': new['Produk'], 'Harga': new['Harga']})
    print(f">1. Update lagi\n>0. Kembali\n{'='*40}")
    while True:
        inputan = input("Pilihan >")
        if inputan == "1":
            updateKatalog(excel)
        elif inputan == "0":
            katalogAdmin()

def dataTransaksi():
    """Data produk yang dibeli users"""
    List = []
    if not os.path.exists("Transaksi.csv"):
         while True:
            inputan = input("Tidak ada stok. Tekan enter untuk kembali...")
            if inputan == "":
                menuAdmin()
    else:
        with open("Transaksi.csv", "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                List.append(row)
    data = pd.DataFrame(List)
    clear()
    print(f"{'Update Status'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    print(f">1. Ubah status\n>0. Kembali\n{'='*40}")
    x=0
    while x == 0:
        x=1
        pilihan = input("Pilihan >")
        if pilihan == "1":
            clear()
            print(f"{'Update Status'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
            a=1
            while a==1:
                a=0
                nomer = input("Id yang di ubah >")
                if nomer.isdigit():
                    nomer=int(nomer)
                else:
                    b=1
                    while b==1:
                        b=0
                        inputan=input("Inputan tidak valid. Tekan enter untuk mengulang")
                        if inputan == "":
                            a=1
                        else:
                            b=1
            print(f">1. Proses\n>2. Terkirim\n{'='*40}")
            f=0
            while f == 0:
                f=1
                inputan = input("Pilihan >")
                if inputan == "1":
                    mode="Proses"
                elif inputan == "2":
                    mode='Terkirim'
                else:
                    f=0
            data.loc[nomer,'Status'] = mode
            dicti = data.to_dict(orient='records')
            with open("Transaksi.csv", "w") as update:
                Top = ['Tanggal', 'Username', 'Produk', 'Jumlah', 'Harga', 'Total', 'Status']
                tambah = csv.DictWriter(update, fieldnames=Top)
                tambah.writeheader()
                for new in dicti:
                    tambah.writerow({'Tanggal': new['Tanggal'], 'Username': new['Username'], 'Produk': new['Produk'], 'Jumlah': new['Jumlah'], 'Harga': new['Harga'], 'Total': new['Total'], 'Status': new['Status']})
            clear()
            print(f"{'Update Status'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
            print(f">1. Ubah status\n>0. Kembali\n{'='*40}")
            while True:
                inputan = input("Pilihan >")
                if inputan == "1":
                    dataTransaksi()
                elif inputan == "0":
                    menuAdmin()
        elif pilihan == "0":
            menuAdmin()
        else:
            x=0

def dataMasukan():
    """Data masukan users"""
    List = []
    if not os.path.exists("Data_masukan.csv"):
        while True:
            inputan = input("Tidak ada stok. Tekan enter untuk kembali...")
            if inputan == "":
                menuAdmin()
    else:
        with open("Data_masukan.csv", "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                List.append(row)
        data = pd.DataFrame(List)
    clear()
    print(f"{'Data masukan'.center(40)}\n{'='*40}\n{data.to_string(max_colwidth=None)}\n{'='*40}")
    while True:
        inputan = input("Tekan enter untuk kembali")
        if inputan == "":
            menuAdmin()


def konsultasiAdmin():
    """Menu Data Konsultasi Admin"""
    clear()
    print(f"{'Data Konsultasi'.center(40)}\n{'='*40}")
    def tampilan(excel,logo):
        if not os.path.exists(excel):
            print(f"{'Tidak ada data konsultasi'.center(40)}\n{'='*40}")
        else:
            print(f"{logo.center(40)}\n{'='*40}")
            List = []
            with open(excel, "r") as see:
                lihat = csv.DictReader(see)
                for row in lihat:
                    List.append(row)
                data = pd.DataFrame(List)
                print(f"{data.to_string(max_colwidth=None)}\n{'='*40}")
    tampilan("Konsultasi Bibit.csv","Bibit")
    tampilan("Konsultasi Hama.csv","Hama")
    print(f">1. Tambah konsultasi\n>2. Hapus konsultasi\n>3. Update konsultasi\n>0. Kembali")
    while True:
        inputan = input("Pilihan >")
        if inputan == "0":
            menuAdmin()
        inputan2= input("Hama/Bibit >")
        if inputan == "1":
            if inputan2 == "Hama":
                tambahKonsul("Konsultasi Hama.csv")
            elif inputan2 == "Bibit":
                tambahKonsul("Konsultasi Bibit.csv")
        elif inputan == "2":
            if inputan2 == "Hama":
                hapuskonsul("Konsultasi Hama.csv")
            elif inputan2 == "Bibit":
                hapuskonsul("Konsultasi Bibit.csv")
        elif inputan == "3":
            if inputan2 == "Hama":
                updateKonsul("Konsultasi Hama.csv")
            elif inputan2 == "Bibit":
                updateKonsul("Konsultasi Bibit.csv")

def tambahKonsul(name):
    """Tambah data dalam csv yang ditentukan"""
    clear()
    print(f"{'Tambah Data Konsultasi'.center(40)}\n{'='*40}")
    List = []
    if os.path.exists(name):
        with open(name, "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                List.append(row)
    x=0
    while x == 0:
        x=1
        if name == "Konsultasi Bibit.csv":
            nama=input("Masukkan nama bibit >")
            a=1
            while a==1:
                a=0
                try:
                    Min = int(input("Masukkan suhu minimal (Celcius) >"))
                except ValueError:
                    a=1
            a=1
            while a==1:
                a=0
                try:
                    Max = int(input("Masukkan suhu maximal (Celcius) >"))
                except ValueError:
                    a=1
            a=1
            while a==1:
                a=0
                try:
                    bentar = int(input("Masukkan lama waktu tanam tercepat (hari) >"))
                except ValueError:
                    a=1
            a=1
            while a==1:
                a=0
                try:
                    lama = int(input("Masukkan lama waktu tanam terlama (hari) >"))
                except ValueError:
                    a=1
        elif name == "Konsultasi Hama.csv":
            nama=input("Masukkan nama hama >")
            solusi=input("Masukkan solusi >")
        for row in List:
            if name == "Konsultasi Bibit.csv":
                if row['Produk'] == nama:
                    print(f"{'Data susah ada'.center(40)}\n>1. Tambah data lain\n>0. Kembali")
                    y=0
                    while y==0:
                        y=1
                        inputan=input("Pilihan >")
                        if inputan == "1":
                            tambahKonsul(name)
                        elif inputan == "0":
                            konsultasiAdmin()
                        else:
                            y=0
            elif name == "Konsultasi Hama.csv":
                if row['Hama'] == nama:
                    print(f"{'Data susah ada'.center(40)}\n>1. Tambah data lain\n>0. Kembali")
                    y=0
                    while y==0:
                        y=1
                        inputan=input("Pilihan >")
                        if inputan == "1":
                            tambahKonsul(name)
                        elif inputan == "0":
                            konsultasiAdmin()
                        else:
                            y=0
        if name == "Konsultasi Bibit.csv":
            List.append({'Produk': nama, 'SuhuMin': Min, 'SuhuMax': Max, 'Cepat': bentar, 'Lama': lama})
            with open(name, "w") as tambah:
                Top = ['Produk', 'SuhuMin', 'SuhuMax', 'Cepat', 'Lama']
                tambah = csv.DictWriter(tambah, fieldnames=Top)
                tambah.writeheader()
                for i in List:
                    tambah.writerow({'Produk': i['Produk'], 'SuhuMin': i['SuhuMin'], 'SuhuMax': i['SuhuMax'], 'Cepat': i['Cepat'], 'Lama': i['Lama']})
        elif name == "Konsultasi Hama.csv":
            List.append({'Hama': nama, 'Produk': solusi})
            with open(name, "w") as tambah:
                Top = ['Hama', 'Produk']
                tambah = csv.DictWriter(tambah, fieldnames=Top)
                tambah.writeheader()
                for i in List:
                    tambah.writerow({'Hama': i['Hama'], 'Produk': i['Produk']})
    print(f">1. Tambah data lagi\n>0. Kembali")
    while True:
        inputan=input("Pilihan >")
        if inputan == "1":
            tambahKonsul(name)
        elif inputan == "0":
            konsultasiAdmin()

def hapuskonsul(name):
    """Hapus data dalam csv yang ditentukan"""
    List=[]
    listindex=[]
    count= 0
    if not os.path.exists(name):
        while True:
            inputan = input("Tidak ada data. Tekan enter untuk kembali...")
            if inputan == "":
                konsultasiAdmin()
    else:
        with open(name, "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                List.append(row)
                listindex.append(count)
                count+=1
    del listindex[count-1]
    data = pd.DataFrame(List)
    clear()
    print(f"{'Hapus Data Konsultasi'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    a=1
    while a==1:
        a=0
        try:
            inputan = int(input("Nomer yang ingin dihapus >"))
        except ValueError:
            a=1
    data = data.drop(inputan)
    data.index = listindex
    dicti = data.to_dict(orient='records')
    if name == "Konsultasi Bibit.csv":
        with open(name, "w") as news:
            Top = ['Produk', 'SuhuMin', 'SuhuMax', 'Cepat', 'Lama']
            tambah = csv.DictWriter(news, fieldnames=Top)
            tambah.writeheader()
            for i in dicti:
                tambah.writerow({'Produk': i['Produk'], 'SuhuMin': i['SuhuMin'], 'SuhuMax': i['SuhuMax'], 'Cepat': i['Cepat'], 'Lama': i['Lama']})
    elif name == "Konsultasi Hama.csv":
        with open(name, "w") as news:
            Top = ['Hama', 'Produk']
            tambah = csv.DictWriter(news, fieldnames=Top)
            tambah.writeheader()
            for i in dicti:
                tambah.writerow({'Hama': i['Hama'], 'Produk': i['Produk']})
    clear()
    print(f"{'Hapus Data Konsultasi'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    print(f">1. Hapus lagi\n>0. Kembali")
    while True:
        inputan = input("Pilihan >")
        if inputan == "1":
            hapuskonsul(name)
        elif inputan == "0":
            konsultasiAdmin()

def updateKonsul(name):
    """Update data dalam csv yang ditentukan"""
    List=[]
    count=0
    if not os.path.exists(name):
        while True:
            inputan = input("Tidak ada data. Tekan enter untuk kembali...")
            if inputan == "":
                konsultasiAdmin()
    else:
        with open(name, "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                List.append(row)
                count+=1
    data = pd.DataFrame(List)
    clear()
    print(f"{'Update Data Konsultasi'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    a=1
    while a==1:
        a=0
        baris = input("Pilih nomer barang yang ingin diganti >")
        if baris.isdigit():
            baris=int(baris)
            if baris > count-1:
                b=1
                while b==1:
                    b=0
                    inputan=input("Inputan tidak valid. Tekan enter untuk mengulang...")
                    if inputan == "":
                        a=1
                    else:
                        b=1
        else:
            c=1
            while c==1:
                c=0
                inputan=input("Inputan tidak valid. Tekan enter untuk mengulang")
                if inputan == "":
                    a=1
                else:
                    c=1
    d=1
    while d==1:
        jenis = input("jenis yang ingin diganti >")
        if jenis == "Produk" or jenis == "SuhuMin" or jenis == "SuhuMax" or jenis == "Cepat" or jenis == "Lama" or jenis == "Hama":
            d=0
        else:
            e=1
            while e==1:
                e=0
                inputan=input("Inputan tidak valid. Tekan enter untuk mengulang...")
                if inputan == "":
                    d=1
                else:
                    e=1
    f=1
    while f == 1:
        f=0
        baru = input("Data yang baru >")
        if baru == "":
            g=1
            while g==1:
                g=0
                inputan= input("Inputan tidak valid. Tekan enter untuk mengulang...")
                if inputan == "":
                    f=1
                else:
                    g=1
    data.loc[baris,jenis] = baru
    dicti = data.to_dict(orient='records')
    if name == "Konsultasi Bibit.csv":
        with open("Konsultasi Bibit.csv", "w") as news:
            Top = ['Produk', 'SuhuMin', 'SuhuMax', 'Cepat', 'Lama']
            tambah = csv.DictWriter(news, fieldnames=Top)
            tambah.writeheader()
            for i in dicti:
                tambah.writerow({'Produk': i['Produk'], 'SuhuMin': i['SuhuMin'], 'SuhuMax': i['SuhuMax'], 'Cepat': i['Cepat'], 'Lama': i['Lama']})
    elif name == "Konsultasi Hama.csv":
        with open(name, "w") as news:
            Top = ['Hama', 'Produk']
            tambah = csv.DictWriter(news, fieldnames=Top)
            tambah.writeheader()
            for i in List:
                tambah.writerow({'Hama': i['Hama'], 'Produk': i['Produk']})
    clear()
    print(f"{'Update Data Konsultasi'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    print(f">1. Update\n>0. Kembali")
    while True:
        inputan = input("Pilihan >")
        if inputan == "1":
            updateKonsul(name)
        elif inputan == "0":
            konsultasiAdmin()

# USERS======================================================================================================================================
def konsultasi(dataUser):
    """Konsultasi users"""
    clear()
    print(f"{'Konsultasi'.center(40)}\n{'='*40}")
    List=[]
    hasilList=[]
    print(f">1. Bibit\n>2. Hama\n>0. Kembali\n{'='*40}")
    x=0
    while x==0:
        x=1
        inputan=input("Pilihan >")
        if inputan == "1":
            excel="Konsultasi Bibit.csv"
        elif inputan == "2":
            excel="Konsultasi Hama.csv"
        elif inputan == "0":
            menu(dataUser)
        else:
            x=0
    if not os.path.exists(excel):
        while True:
            inputan = input("Tidak ada stok. Tekan enter untuk kembali...")
            if inputan == "":
                konsultasi(dataUser)
    else:
        with open(excel, "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                List.append(row)
    if excel == "Konsultasi Bibit.csv":
        iSuhu=(input("Masukkan suhu daerah pertanian >"))
        iLama=(input("Masukkan lama waktu tumbuh >"))
        for row in List:
            if iSuhu != "":
                if int(row['SuhuMin'])<=int(iSuhu)<=int(row['SuhuMax']):
                    if iLama != "":
                        if int(row['Cepat'])<=int(iLama)<=int(row['Lama']):
                            hasilList.append(row)
                    else:
                        hasilList.append(row)
            else:
                if iLama != "":
                    if int(row['Cepat'])<=int(iLama)<=int(row['Lama']):
                        hasilList.append(row)
                else:
                    hasilList.append(row)
        if hasilList != []:    
            print(hasilList)
            hasil = pd.DataFrame(hasilList)
            clear()
            print(f"{'Konsultasi Bibit'.center(40)}\n{'='*40}")
            print(f"Suhu        : {iSuhu} Celsius\nMasa tumbuh : {iLama} hari\n{'='*40}\n{hasil}\n{'='*40}")
            print(f">1. Konsultasi\n>2. Pembelian\n>0. Kembali\n{'='*40}")
            while True:
                inputan=input("Pilihan >")
                if inputan == "1":
                    konsultasi(dataUser)
                elif inputan == "2":
                    pembelian2(dataUser,hasil)
                elif inputan == "0":
                    menu(dataUser)
        else:
            clear()
            print(f"{'Konsultasi Bibit'.center(40)}\n{'='*40}")
            print(f"Suhu        : {iSuhu} Celcius\nMasa tumbuh : {iLama} hari\n{'='*40}")
            print(f"{'Data tidak ada'.center(40)}\n{'='*40}\n>1. Konsultasi\n>0. Kembali")
            while True:
                inputan=input("Pilihan >")
                if inputan == "1":
                    konsultasi(dataUser)
                elif inputan == "0":
                    menu(dataUser)
    elif excel == "Konsultasi Hama.csv":
        data=pd.DataFrame(List)
        tampilan=data[['Hama']].drop_duplicates()
        hasil=[]
        clear()
        print(f"{'Konsultasi Hama'.center(40)}\n{'='*40}")
        print(f"{tampilan}\n{'='*40}")
        pilihan=int(input("Pilih nomer hama >"))
        for row in List:
            if row['Hama'] == tampilan.at[pilihan,'Hama']:
                hasil.append(row)
        hasil = pd.DataFrame(hasil)
        clear()
        print(f"{'Konsultasi Hama'.center(40)}\n{'='*40}")
        print(f"Solusi hama : {tampilan.at[pilihan,'Hama']}\n{'='*40}\n{hasil[['Produk']]}\n{'='*40}")
        print(f">1. Konsultasi\n>2. Pembelian\n>0. Kembali\n{'='*40}")
        while True:
                inputan=input("Pilihan >")
                if inputan == "1":
                    konsultasi(dataUser)
                elif inputan == "2":
                    print("proses")
                    pembelian2(dataUser,hasil)
                elif inputan == "0":
                    menu(dataUser)

def pembelian2(dataUser,hasil):
    """Pembelian setelah konsultasi"""
    List=[]
    nomer=0
    tanggal = datetime.now()
    tanggal = tanggal.strftime("%d-%m-%Y")
    clear()
    print(f"{'Pembelian'.center(40)}\n{'='*40}")
    if os.path.exists("gudang.csv"):
        with open("gudang.csv", "r") as see:
            lihat=csv.DictReader(see)
            for row in lihat:
                List.append(row)
    produk=hasil[['Produk']]
    detail=pd.DataFrame(List)
    gabungan = pd.merge(produk,detail,on='Produk')
    for i in gabungan['Produk']:
        nomer+=1
    print(f"{gabungan}\n{'='*40}")
    a=1
    while a==1:
        a=0
        nomerBarang = input("Nomer barang yang ingin dibeli >")
        if nomerBarang.isdigit():
            nomerBarang=int(nomerBarang)
            if nomerBarang > nomer-1:
                b=1
                while b==1:
                    b=0
                    inputan=input("Inputan tidak valid. Tekan enter untuk mengulang...")
                    if inputan == "":
                        a=1
                    else:
                        b=1
        else:
            c=1
            while c==1:
                c=0
                inputan=input("Inputan tidak valid. Tekan enter untuk mengulang...")
                if inputan == "":
                    a=1
                else:
                    c=1
    b=1
    while b == 1:
        b=0
        try:
            jumlahBarang = int(input("Jumlah yang ingin dibeli >"))
            if jumlahBarang <= 0:
                c=1
                while c==1:
                    c=0
                    inputan = input("Jumlah tidak valid. Silahkan masukkan jumlah barang kembali...")
                    if inputan=="":
                        b=1
                    else:
                        c=1
        except ValueError:
            b=1
    count=0
    for data in List:
        if gabungan.at[nomerBarang,'Produk'] == data['Produk']:
            h=1
            while h==1:
                h=0
                if jumlahBarang <= int(data['Jumlah']):
                    totalHarga = jumlahBarang*int(data['Harga'])
                    detail.loc[count,'Jumlah'] = int(detail.at[count,'Jumlah'])-jumlahBarang
                    if not os.path.exists("Transaksi.csv"):
                        Top  = ['Tanggal', 'Username', 'Produk', 'Jumlah', 'Harga', 'Total', 'Status']
                        with open("Transaksi.csv", "w") as make:
                            buat = csv.writer(make)
                            buat.writerow(Top)
                    with open("Transaksi.csv", "a") as add:
                        Top = ['Tanggal', 'Username', 'Produk', 'Jumlah', 'Harga', 'Total', 'Status']
                        tambah = csv.DictWriter(add, fieldnames=Top)
                        tambah.writerow({'Tanggal': tanggal, 'Username': dataUser[0], 'Produk': data['Produk'], 'Jumlah': jumlahBarang, 'Harga': data['Harga'], 'Total': totalHarga, 'Status': "Proses"})
                    dictgudang = detail.to_dict(orient='records')
                    with open("gudang.csv", "w") as update:
                        top = ['Produk', 'Jumlah', 'Harga']
                        baru = csv.DictWriter(update, fieldnames=top)
                        baru.writeheader()
                        for new in dictgudang:
                            baru.writerow({'Produk': new['Produk'], 'Jumlah': new['Jumlah'], 'Harga': new['Harga']})
                    print(f"{'='*40}\n{'Pemesanan Berhasil'.center(40)}\n>1. Konsultasi\n>0. Kembali\n{'='*40}")
                    while True:
                        inputan=input("Pilihan >")
                        if inputan == "1":
                            konsultasi(dataUser)
                        elif inputan == "0":
                            menu(dataUser)
        count+=1

def pembelian(dataUser):
    """Pembelian menampilkan katalog"""
    tanggal = datetime.now()
    tanggal = tanggal.strftime("%d-%m-%Y")
    listKatalog = []
    listGudang = []
    nomer=0
    clear()
    print(f"{'Pembelian'.center(40)}\n{'='*40}\n>1. Bibit\n>2. Pupuk\n>3. Pestisida")
    x = 1
    while x == 1:
        x=0
        inputan = input("Pilihan >")
        if inputan == "1":
            file="bibit.csv"
        elif inputan == "2":
            file="pupuk.csv"
        elif inputan == "3":
            file="pestisida.csv"
        else:
            x=1
    if os.path.exists("gudang.csv"):
        with open("gudang.csv", "r") as cek:
            lihat = csv.DictReader(cek)
            for row in lihat:
                listGudang.append(row)
        dataGudang = pd.DataFrame(listGudang)
    if not os.path.exists(file):
        while True:
            inputan = input("Tidak ada katalog. Tekan enter untuk kembali...")
            if inputan == "":
                menu(dataUser)
    else:
        with open(file, "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                listKatalog.append(row)
            dataKatalog = pd.DataFrame(listKatalog)
    gabungan = pd.merge(dataGudang[['Produk', 'Jumlah']], dataKatalog, on='Produk')
    clear()
    print(f"{'Pembelian'.center(40)}\n{'='*40}\n{gabungan.to_string(max_colwidth=None)}\n{'='*40}")
    nomerBarang = int(input("Nomer barang yang ingin dibeli >"))
    b=1
    while b == 1:
        b=0
        jumlahBarang = int(input("Jumlah yang ingin dibeli >"))
        if jumlahBarang <= 0:
            c=1
            while c==1:
                c=0
                inputan = input("Jumlah tidak valid. Silahkan masukkan jumlah barang kembali...")
                if inputan=="":
                    b=1
                else:
                    c=1
    count = 0
    for data in listGudang:
        if listKatalog[nomerBarang]['Produk'] == data['Produk']:
            h=1
            while h == 1:
                h=0
                if jumlahBarang <= int(data['Jumlah']):
                    totalHarga = jumlahBarang*int(data['Harga'])
                    dataGudang.loc[count,'Jumlah'] = int(dataGudang.at[count,'Jumlah'])-jumlahBarang
                    if not os.path.exists("Transaksi.csv"):
                        Top = ['Tanggal', 'Username', 'Produk', 'Jumlah', 'Harga', 'Total', 'Status']
                        with open("Transaksi.csv", "w") as make:
                            buat = csv.writer(make)
                            buat.writerow(Top)
                    with open("Transaksi.csv", "a") as add:
                        Top = ['Tanggal', 'Username', 'Produk', 'Jumlah', 'Harga', 'Total', 'Status']
                        tambah = csv.DictWriter(add, fieldnames=Top)
                        tambah.writerow({'Tanggal': tanggal, 'Username': dataUser[0], 'Produk': data['Produk'], 'Jumlah': jumlahBarang, 'Harga': data['Harga'], 'Total': totalHarga, 'Status': "Proses"})
                    dictiGudang = dataGudang.to_dict(orient='records')
                    with open("gudang.csv", "w") as update:
                        top = ['Produk', 'Jumlah', 'Harga']
                        baru = csv.DictWriter(update, fieldnames=top)
                        baru.writeheader()
                        for new in dictiGudang:
                            baru.writerow({'Produk': new['Produk'], 'Jumlah': new['Jumlah'], 'Harga': new['Harga']})
                    print(f"{'='*40}\n{'Pembelian berhasil'.center(40)}\n>1. Beli barang lagi\n>0. Kembali")
                    while True:
                        inputan = input("Pilihan >")
                        if inputan == "1":
                            pembelian(dataUser)
                        elif inputan == "0":
                            menu(dataUser)
                print(f"{'Stok tidak cukup'}\n>1. Masukkan jumlah\n>2. Beli barang lain\n>0. Kembali")
                a=1
                while a == 1:
                    a=0
                    pilihan = input("Pilihan >")
                    if pilihan == "1":
                        h=1
                    elif pilihan == "2":
                        pembelian(dataUser)
                    elif pilihan == "0":
                        menu(dataUser)
                    else:
                        a=1
        count+=1
    print(f"{'Stok tidak ada'}\n>1. Beli barang lain\n>0. Kembali")
    while True:
        pilihan = input("Pilihan >")
        if pilihan == "1":
            pembelian(dataUser)
        elif pilihan == "0":
            menu(dataUser)

def masukan(dataUser):
    """Memberikan masukan/kritik dari users"""
    clear()
    print(f"{'Masukan'.center(40)}\n{'='*40}")
    tanggal = datetime.now()
    tanggal = tanggal.strftime("%d-%m-%Y")
    a=1
    while a==1:
        a=0
        kata2 = input("Silahkan ketik masukan anda >")
        if kata2 == "":
            b=1
            while b==1:
                b=0
                inputan=input("Masukan tidak valid. Tekan enter untuk mengulang...")
                if inputan == "":
                    a=1
                else:
                    b=1
    if not os.path.exists("Data_masukan.csv"):
        Top = ['Tanggal', 'User', 'Masukan']
        with open("Data_masukan.csv", "w") as make:
            buat = csv.writer(make)
            buat.writerow(Top)
        with open("Data_masukan.csv", "a") as add:
            Top = ['Tanggal', 'User', 'Masukan']
            tambah = csv.DictWriter(add, fieldnames=Top)
            tambah.writerow({'Tanggal': tanggal, 'User': dataUser[0], 'Masukan': kata2})
    print (f"{'Masukan berhasil dikirim'.center(40)}")
    while True:
        inputan = input("Tekan enter untuk kembali...")
        if inputan == "":
            menu(dataUser)

def transaksiUser(dataUser):
    List = []
    if not os.path.exists("Transaksi.csv"):
        while True:
            inputan = input("Tidak ada pembelian. Tekan enter untuk kembali...")
            if inputan == "":
                menu(dataUser)
    else:
        with open("Transaksi.csv", "r") as see:
            lihat = csv.DictReader(see)
            for row in lihat:
                if row['Username'] == dataUser[0]:
                    List.append(row)
            data=pd.DataFrame(List)
    clear()
    print(f"{'Transaksi'.center(40)}\n{'='*40}\n{data}\n{'='*40}")
    while True:
        inputan = input("Tekan enter untuk kembali...")
        if inputan == "":
            menu(dataUser)

def menu(dataUser):
    clear()
    print(f"{'Menu'.center(40)}\n{'='*40}")
    print(f">1. konsultasi\n>2. Pembelian\n>3. Transaksi\n>4. Masukan\n>5. Bantuan\n>0. Keluar")
    while True:
        pilihan=input("Pilihan >")
        if pilihan == "1":
            konsultasi(dataUser)
        elif pilihan == "2":
            pembelian(dataUser)
        elif pilihan == "3":
            transaksiUser(dataUser)
        elif pilihan == "4":
            masukan(dataUser)
        elif pilihan == "5":
            bantuan(dataUser)
        elif pilihan == "0":
            pilihan_login()

def pilihan_login():
    """Tampilan awal"""
    os.system('cls')
    print("""
  ______                   _____           __  __            _   
 |  ____|                 |  __ \         |  \/  |          | |  
 | |__ __ _ _ __ _ __ ___ | |__) | __ ___ | \  / | __ _ _ __| |_ 
 |  __/ _` | '__| '_ ` _ \|  ___/ '__/ _ \| |\/| |/ _` | '__| __|
 | | | (_| | |  | | | | | | |   | | | (_) | |  | | (_| | |  | |_ 
 |_|  \__,_|_|  |_| |_| |_|_|   |_|  \___/|_|  |_|\__,_|_|   \__|
                                                                                                                          
""")
    print(f"{'='*65}\n> login\n> daftar\n> exit")
    pilihan=input("Pilihan >")
    if pilihan=="login":
        login()
    elif pilihan=="daftar":
        daftar()
    elif pilihan=="exit":
        exit()
    else:
        pilihan_login()

def bantuan(dataUser):
    clear()
    print(f"{'Menu Bantuan'.center(40)}\n{'='*40}")
    print(f"1. Bagaimana cara menggunakan fitur Konsultasi?\n2. Apa metode pembayaran yang dapat saya gunakan?\n3. Bagaimana cara membuat akun baru?\n4. Bagaimana cara saya menyampaikan keluhan tentang aplikasi farmpro.mart ini?\n5. Bagaimana saya bisa menghubungi layanan pelanggan?")
    inputan = input("Pilihan >")
    if inputan == "1" :
        clear()
        print(f"{'Menu Bantuan'.center(40)}\n{'='*40}")
        print(f"Cara menggunakan fitur konsultasi :\n1. Pilih fitur konsultasi\n2. Pilih keluhan (Hama/Bibit)\n3. Jika memilih hama, masukkan jenis hama apa yang menyerang lahan pertanian, lalu program akan memberikan rekomendasi produk pestisida secara otomatis\n4. Jika memilih bibit, masukkan berapa derajat suhu daerah lahan dan juga lama waktu panen yang diharapkan. Program akan secara otomatis memberikan rekomendasi bibit yang sesuai dengan lahan dan lama waktu yang diinginkan pengguna\n5. Produk rekomendasi dapat langsung dibeli oleh pengguna tanpa harus kembali ke fitur pembelian")
    elif inputan == "2" :
        clear()
        print(f"{'Menu Bantuan'.center(40)}\n{'='*40}")
        print("Program kami hanya menyediakan metode pembayaran cash on delivery")
    elif inputan == "3":
        clear()
        print(f"{'Menu Bantuan'.center(40)}\n{'='*40}")
        print(f"Cara membuat akun baru :\n1. Pada tampilan awal, pilih registrasi\n2. Masukkan username dan password baru\n3. Akun berhasil dibuat")
    elif inputan == "4":
        clear()
        print(f"{'Menu Bantuan'.center(40)}\n{'='*40}")
        print("Pada aplikasi farmpro.mart telah disediakan fitur masukan untuk pengguna menyampaikan kritik dan saran tentang program aplikasi farmpro.mart")
    elif inputan == "5":
        clear()
        print(f"{'Menu Bantuan'.center(40)}\n{'='*40}")
        print(f"Anda dapat menghubungi cp yang tertera dibawah ini : \n+6281234567890")
    else :
        b=1
        while b==1:
            b=0
            inputan = input("Inputan tidak valid. Tekan enter untuk mengulang...")
            if inputan == "":
                bantuan(dataUser)
            else:
                b=1
    print(f"{'='*40}\n>1. Tanya lagi \n>0. Kembali")
    while True:
        inputan = input("Pilihan >")
        if inputan == "1":
            bantuan(dataUser)
        elif inputan == "0":
            menu(dataUser)

pilihan_login()