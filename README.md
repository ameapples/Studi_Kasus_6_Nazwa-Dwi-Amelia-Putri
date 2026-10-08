# Sistem Manajemen Inventaris Barang

> Nama: Nazwa Dwi Amelia Putri
> 
> NIM: 008
> 
> Kelas: A


Ini adalah program yang saya buat menggunakan Python untuk mengelola data inventaris barang melalui terminal (CLI). Program ini adalah penugasan Studi Kasus 6 pada praktikum Dasar-Dasar Pemrograman. Semua data barang saya simpan di file JSON, jadi data tidak hilang ketika program ditutup.

## Fitur

- **Tampilkan Data Barang**: menampilkan seluruh barang dalam bentuk tabel (kode, nama, stok, harga).
- **Tambah Barang Baru**: menambahkan barang baru lengkap dengan validasi input.
- **Penyimpanan Otomatis**: data disimpan ke file `inventaris.json`, dan file dibuat otomatis jika belum ada.
- **Menu Interaktif**: menu utama akan terus tampil sampai pengguna memilih keluar.

## Persyaratan

- Python 3.x (saya menjalankannya pada Python 3.11)
- Tidak memerlukan library tambahan, saya hanya memakai modul bawaan `json` dan `os`

## Cara Menjalankan

1. Simpan file `Studi Kasus 6.py` pada sebuah folder.
2. Buka terminal pada folder tersebut.
3. Jalankan perintah:

   ```bash
   python "Studi Kasus 6.py"
   ```

## Cara Penggunaan

Setelah program dijalankan, menu utama akan tampil:

```
================================
 SISTEM MANAJEMEN INVENTARIS
================================
1. Tampilkan Data Barang
2. Tambah Barang Baru
3. Keluar
================================
Pilih menu (1-3):
```

| Menu | Fungsi |
|------|--------|
| 1 | Menampilkan semua data barang dalam tabel |
| 2 | Menambah barang baru (kode, nama, stok, harga) |
| 3 | Mengakhiri program |

### Contoh Menambah Barang

```
Pilih menu (1-3): 2

===== TAMBAH BARANG BARU =====
Masukkan kode barang: B003
Masukkan nama barang: Pensil
Masukkan jumlah stok: 25
Masukkan harga barang: 2500
Barang berhasil ditambahkan dan disimpan!
```

### Contoh Tampilan Data

```
===== DATA INVENTARIS BARANG =====
-----------------------------------------------------------------
Kode      Nama Barang         Stok      Harga
-----------------------------------------------------------------
B001      Buku Tulis          20        Rp5000
B002      Pulpen              15        Rp3000
B003      Pensil              25        Rp2500
-----------------------------------------------------------------
```

## Penjelasan Kode Program

### 1. Import modul dan persiapan file

```python
import json
import os

nama_file = "inventaris.json"

if not os.path.exists(nama_file):
    with open(nama_file, "w") as file:
        json.dump([], file)
```

- Saya mengimpor `json` untuk membaca dan menulis data berformat JSON.
- Saya mengimpor `os` untuk memeriksa apakah sebuah file sudah ada.
- Variabel `nama_file` saya gunakan untuk menyimpan nama file tempat data inventaris disimpan.
- `os.path.exists(nama_file)` saya pakai untuk mengecek keberadaan file. Jika belum ada, file dibuat dengan mode `"w"` (write) dan diisi list kosong `[]` memakai `json.dump()`. Dengan begitu program tidak error saat pertama kali dijalankan.
- Saya memakai `with open(...)` agar file otomatis tertutup setelah blok selesai.

### 2. Function `baca_data()`

```python
def baca_data():
    with open(nama_file, "r") as file:
        return json.load(file)
```

Function ini membuka file dalam mode `"r"` (read), lalu `json.load()` mengubah isi JSON menjadi **list berisi dictionary** Python. Saya membuatnya sebagai function tersendiri supaya kode pembacaan data tidak perlu saya tulis berulang di `tampilkan_barang()` dan `tambah_barang()`.

### 3. Function `tampilkan_barang()`

```python
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
```

- Pertama, data dibaca dengan `baca_data()`.
- `len(data_barang) == 0` saya gunakan untuk memeriksa apakah data masih kosong. Jika ya, program menampilkan "Belum ada data barang."
- `"-" * 65` mengulang karakter `-` sebanyak 65 kali untuk membuat garis pemisah tabel.
- Format `{'Kode':<10}` membuat teks rata kiri (`<`) dengan lebar 10 karakter, sehingga kolom tabel sejajar dan rapi.
- Perulangan `for barang in data_barang` mengambil setiap dictionary barang, lalu mencetak `kode`, `nama`, `stok`, dan `harga` dengan lebar kolom yang sama seperti header.

### 4. Function `tambah_barang()`

**a. Input dan validasi kosong**

```python
kode = input("Masukkan kode barang: ").strip()
nama = input("Masukkan nama barang: ").strip()
if not kode or not nama:
    print("Kode dan nama barang tidak boleh kosong!")
    return
```

`.strip()` saya pakai untuk menghapus spasi di awal dan akhir input. Jika kode atau nama kosong, function berhenti dengan `return` dan pengguna kembali ke menu.

**b. Cek kode duplikat**

```python
data_barang = baca_data()

for barang in data_barang:
    if barang["kode"].lower() == kode.lower():
        print("Kode barang sudah terdaftar!")
        return
```

Saya membaca data lama, lalu membandingkan setiap kode dengan kode yang baru dimasukkan. `.lower()` mengubah huruf menjadi kecil sehingga `B001` dan `b001` dianggap sama. Jika ditemukan kode yang sama, barang tidak ditambahkan.

**c. Input stok dan harga**

```python
try:
    stok = int(input("Masukkan jumlah stok: "))
    harga = int(input("Masukkan harga barang: "))
    if stok < 0 or harga < 0:
        print("Stok dan harga tidak boleh negatif!")
        return
except ValueError:
    print("Stok dan harga harus berupa angka!")
    return
```

`int()` mengubah input teks menjadi bilangan bulat. Jika pengguna mengetik huruf atau angka desimal, Python melempar `ValueError` yang saya tangkap dengan `except`, sehingga program tidak crash. Nilai negatif juga saya tolak.

**d. Menyimpan data**

```python
barang_baru = {"kode": kode, "nama": nama, "stok": stok, "harga": harga}
data_barang.append(barang_baru)

with open(nama_file, "w") as file:
    json.dump(data_barang, file, indent=4)

print("Barang berhasil ditambahkan dan disimpan!")
```

Barang baru saya buat sebagai dictionary, lalu ditambahkan ke list dengan `append()`. Seluruh list kemudian ditulis ulang ke file JSON memakai `json.dump()`. Parameter `indent=4` membuat isi file rapi dan mudah dibaca.

### 5. Menu utama

```python
while True:
    print("\n================================")
    print(" SISTEM MANAJEMEN INVENTARIS")
    ...
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
```

- `while True` membuat menu tampil terus-menerus.
- Pilihan pengguna diperiksa dengan `if-elif-else`: pilihan 1 memanggil `tampilkan_barang()`, pilihan 2 memanggil `tambah_barang()`, dan pilihan 3 menghentikan perulangan dengan `break`.
- Selain 1, 2, atau 3, program menampilkan pesan bahwa pilihan tidak valid.

## Penjelasan Output Program

Berikut penjelasan hasil eksekusi program yang saya jalankan di terminal VS Code.

### Output 1: Menambah barang dengan kode yang sudah terdaftar

<img width="1366" height="768" alt="Screenshot (200)" src="https://github.com/user-attachments/assets/aa1d9a7a-8d30-4870-8bcc-62818917fd43" />

```
Pilih menu (1-3): 2

===== TAMBAH BARANG BARU =====
Masukkan kode barang: B001
Masukkan nama barang: Buku Tulis
Kode barang sudah terdaftar!
```

- Saya memilih menu **2** untuk menambah barang, lalu mengisi kode `B001` dan nama `Buku Tulis`.
- Program langsung menampilkan **"Kode barang sudah terdaftar!"** karena `B001` sudah ada di `inventaris.json`.
- Program tidak menanyakan stok dan harga, karena pengecekan kode duplikat dilakukan sebelum input stok dan harga. Function lalu berhenti dengan `return` dan menu utama tampil lagi.
- Hal yang sama terjadi saat saya memasukkan kode `B002` dengan nama `Pulpen`. Ini membuktikan validasi kode unik berfungsi dan data lama tidak tertimpa.

### Output 2: Menambah barang baru dengan kode yang belum terdaftar

<img width="1366" height="768" alt="Screenshot (201)" src="https://github.com/user-attachments/assets/693f364d-023f-4a38-b814-0010adea2c51" />

```
Pilih menu (1-3): 2

===== TAMBAH BARANG BARU =====
Masukkan kode barang: B003
Masukkan nama barang: Pensil
Masukkan jumlah stok: 25
Masukkan harga barang: 2500
Barang berhasil ditambahkan dan disimpan!
```

- Karena kode `B003` belum ada, program melanjutkan ke input stok (`25`) dan harga (`2500`).
- Semua validasi lolos (angka valid dan tidak negatif), sehingga data ditambahkan ke list dan ditulis ke `inventaris.json`.
- Program menampilkan **"Barang berhasil ditambahkan dan disimpan!"**, lalu kembali ke menu utama.

### Output 3: Menampilkan data barang

```
Pilih menu (1-3): 1

===== DATA INVENTARIS BARANG =====
-----------------------------------------------------------------
Kode      Nama Barang         Stok      Harga
-----------------------------------------------------------------
B001      Buku Tulis          20        Rp5000
B002      Pulpen              15        Rp3000
B003      Pensil              25        Rp2500
-----------------------------------------------------------------
```

- Saya memilih menu **1**, lalu program membaca `inventaris.json` dan menampilkan seluruh barang dalam bentuk tabel.
- Tabel berisi tiga barang: `B001` Buku Tulis (stok 20, Rp5000), `B002` Pulpen (stok 15, Rp3000), dan `B003` Pensil (stok 25, Rp2500).
- Barang `B003` yang baru saya tambahkan sudah muncul di tabel, sehingga terbukti data tersimpan permanen di file JSON.
- Setelah tabel tampil, program kembali menampilkan menu dan menunggu pilihan berikutnya (kursor berkedip di `Pilih menu (1-3):`).

## Ringkasan Struktur Program

| Bagian | Penjelasan |
|--------|------------|
| `nama_file` | Nama file JSON tempat data disimpan (`inventaris.json`) |
| Pengecekan file | Jika file belum ada, dibuat otomatis berisi list kosong `[]` |
| `baca_data()` | Membaca isi file JSON dan mengembalikannya sebagai list of dictionary |
| `tampilkan_barang()` | Membaca data lalu mencetaknya dalam format tabel |
| `tambah_barang()` | Meminta input, memvalidasi, lalu menyimpan barang baru ke file JSON |
| Menu utama | Perulangan `while True` yang memanggil function sesuai pilihan pengguna |

## Validasi Input

Saya menambahkan beberapa validasi pada `tambah_barang()`:

1. Kode dan nama tidak boleh kosong.
2. Kode barang harus unik (tidak membedakan huruf besar/kecil).
3. Stok dan harga harus berupa angka bulat (`try-except ValueError`).
4. Stok dan harga tidak boleh negatif.

Jika ada validasi yang gagal, program menampilkan pesan kesalahan dan kembali ke menu utama.

## Format Data (`inventaris.json`)

```json
[
    {
        "kode": "B001",
        "nama": "Buku Tulis",
        "stok": 20,
        "harga": 5000
    }
]
```

## Konsep Python yang Saya Gunakan

- Function (`def`)
- List dan dictionary
- Perulangan (`for`, `while`)
- Percabangan (`if-elif-else`)
- Penanganan error (`try-except`)
- File handling (`open`, `with`)
- Modul `json` dan `os`
- Formatting string (f-string)

## Catatan

Saya memasukkan kode `B001` dan `B002` yang sudah ada di `inventaris.json`. Program menolaknya dengan pesan **"Kode barang sudah terdaftar!"**, artinya validasi kode unik berjalan dengan benar. Setelah itu saya menambahkan barang baru dengan kode `B003`, dan data berhasil disimpan serta tampil di menu 1.
