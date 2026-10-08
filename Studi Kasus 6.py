import json
import os

# Nama file untuk menyimpan data inventaris
nama_file = "inventaris.json"

# Membuat file JSON jika belum tersedia
if not os.path.exists(nama_file):
    with open(nama_file, "w") as file:
        json.dump([], file)

# Function membaca data barang
def baca_data():
    with open(nama_file, "r") as file:
        return json.load(file)

# Function menampilkan seluruh data barang
def tampilkan_barang():
    data_barang = baca_data()
    print("\n===== DATA INVENTARIS BARANG =====")
    if len(data_barang) == 0:
        print("Belum ada data barang.")
    else:
        print("-" * 65)
        print(f"{'Kode':<10}{'Nama Barang':<20}{'Stok':<10}{'Harga':<15}")
        print("-" * 65)
        for barang in data_barang:
            print(
                f"{barang['kode']:<10}"
                f"{barang['nama']:<20}"
                f"{barang['stok']:<10}"
                f"Rp{barang['harga']:<13}"
            )
        print("-" * 65)

# Function menambahkan barang baru
def tambah_barang():
    print("\n===== TAMBAH BARANG BARU =====")
    kode = input("Masukkan kode barang: ").strip()
    nama = input("Masukkan nama barang: ").strip()
    if not kode or not nama:
        print("Kode dan nama barang tidak boleh kosong!")
        return

    data_barang = baca_data()

    # Memeriksa apakah kode barang sudah digunakan
    for barang in data_barang:
        if barang["kode"].lower() == kode.lower():
            print("Kode barang sudah terdaftar!")
            return

    try:
        stok = int(input("Masukkan jumlah stok: "))
        harga = int(input("Masukkan harga barang: "))
        if stok < 0 or harga < 0:
            print("Stok dan harga tidak boleh negatif!")
            return
    except ValueError:
        print("Stok dan harga harus berupa angka!")
        return

    barang_baru = {"kode": kode, "nama": nama, "stok": stok, "harga": harga}
    data_barang.append(barang_baru)

    # Menyimpan data baru ke dalam file JSON
    with open(nama_file, "w") as file:
        json.dump(data_barang, file, indent=4)

    print("Barang berhasil ditambahkan dan disimpan!")

# Menu utama program
while True:
    print("\n================================")
    print(" SISTEM MANAJEMEN INVENTARIS")
    print("================================")
    print("1. Tampilkan Data Barang")
    print("2. Tambah Barang Baru")
    print("3. Keluar")
    print("================================")
    pilihan = input("Pilih menu (1-3): ")
    if pilihan == "1":
        tampilkan_barang()
    elif pilihan == "2":
        tambah_barang()
    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
