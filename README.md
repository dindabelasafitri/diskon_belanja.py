# kasir_python.git
Mini project Python: program kasir sederhana dengan perhitungan diskon otomatis.

# Kasir Sederhana Update
🛒 Kasir Sederhana (Python)

Proyek ini adalah program Kasir Sederhana berbasis Python untuk mencatat daftar belanja, menghitung diskon, pajak, dan kembalian.
Cocok untuk latihan logika dasar pemrograman, khususnya looping, kondisi, dictionary, dan perhitungan sederhana.

Contoh Alur Program

1. Masukkan data barang:

Nama barang

Harga satuan

Diskon (%)

Jumlah beli

Kategori barang



2. Ulangi jika ingin menambahkan barang lain.


3. Program akan menghitung total belanja, diskon, pajak, lalu menampilkan struk belanja.


4. Masukkan jumlah pembayaran → program akan menghitung kembalian atau memberi pesan jika uang tidak cukup.


✨ Fitur Utama

Input data barang (nama, harga satuan, jumlah, diskon, kategori).

Perhitungan otomatis:

Total harga per barang (harga × jumlah).

Diskon tiap barang (berdasarkan persen diskon).

Pajak 10% dari total belanja.


Format harga dalam Rupiah (contoh: 100000 → Rp 100.000).

Menampilkan struk belanja yang rapi.

Input pembayaran + perhitungan kembalian.


📂 Struktur Data Barang

Setiap barang disimpan dalam bentuk dictionary:

{
  "nama": "Indomie",
  "harga_satuan": 3000,
  "jumlah_beli": 5,
  "total_harga": 15000,
  "diskon_persen": 10,
  "total_diskon": 1500,
  "harga_setelah_diskon": 13500,
  "kategori": "Makanan"
}


⚡ Contoh Output

Data Barang
Nama: Indomie, Harga Satuan: Rp 3.000, Jumlah: 5, Total Harga: Rp 15.000, 
Diskon: 10%, Harga Setelah Diskon: Rp 13.500, Kategori: Makanan

=== STRUK BELANJA ===
Total belanja: Rp 13.500
Jumlah diskon: Rp 1.500
Total setelah diskon: Rp 13.500
Total setelah pajak 10%: Rp 14.850



🚀 Cara Menjalankan Program

1. Clone repo ini

git clone https://github.com/username/diskon_belanja.py
cd nama-repo


2. Jalankan file Python:

python_kasir_sederhana.py

🎯 Tujuan Belajar

Proyek ini dibuat untuk melatih:

Python dasar (input, output, loop, kondisi).

Struktur data dictionary & list.

Logika perhitungan dalam simulasi sederhana kasir.
