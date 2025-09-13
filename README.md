# kasir_python.git
Mini project Python: program kasir sederhana dengan perhitungan diskon otomatis.

# Kasir Sederhana Update
🛒 Kasir Sederhana Python – Versi Member & Multi Transaksi

Project ini adalah mini project Python untuk mencatat belanjaan, menghitung diskon per barang, pajak, diskon member, dan mendukung transaksi berturut-turut. Cocok untuk latihan logika pemrograman, list, dictionary, loop, dan perhitungan sederhana.


---

✨ Fitur Utama

Input nama barang, harga satuan, jumlah beli, diskon per barang, dan kategori barang.

Hitung otomatis:

Total harga per barang

Diskon tiap barang

Pajak 10% dari total belanja

Diskon tambahan 5% untuk kartu member


Menampilkan struk belanja yang rapi

Menampilkan daftar barang berdasarkan kategori

Mendukung transaksi multi-beli, pengguna bisa lanjut input barang baru setelah satu transaksi selesai

Validasi input angka untuk harga, jumlah, dan diskon

Format harga dalam Rupiah (contoh: 100000 → Rp 100.000)

📝 Contoh Alur Program

1. Masukkan data barang:

Nama barang

Harga satuan

Diskon (%)

Jumlah beli

Kategori barang



2. Ulangi jika ingin menambahkan barang lain dalam transaksi yang sama.


3. Program menghitung:

Total belanja

Total diskon

Pajak 10%

Diskon member (jika ada kartu member)



4. Menampilkan struk belanja dan daftar barang berdasarkan kategori.


5. Masukkan jumlah pembayaran → program akan menghitung kembalian atau memberi pesan jika uang tidak cukup.


6. Program menanyakan apakah ingin melakukan transaksi baru. Jika ya, loop kembali ke input barang; jika tidak, program selesai.


📂 Struktur Data Barang

Setiap barang disimpan dalam dictionary:

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

Daftar kategori menyimpan barang sesuai kategorinya, memudahkan tampilan kategori di struk.


---

⚡ Contoh Output

Data Barang
Nama: Indomie, Harga Satuan: Rp 3.000, Jumlah: 5, Total Harga: Rp 15.000,
Diskon: 10%, Harga Setelah Diskon: Rp 13.500, Kategori: Makanan
Nama: Teh, Harga Satuan: Rp 2.000, Jumlah: 10, Total Harga: Rp 20.000,
Diskon: 5%, Harga Setelah Diskon: Rp 19.000, Kategori: Minuman

=== STRUK BELANJA ===
Total belanja: Rp 32.500
Jumlah diskon: Rp 3.500
Total setelah diskon: Rp 32.500
Total setelah pajak 10%: Rp 35.750
Diskon member: Rp 1.787
Total setelah diskon member: Rp 33.963

=== BARANG BERDASARKAN KATEGORI ===
Makanan: Indomie
Minuman: Teh

Masukkan jumlah pembayaran: 40000
Total kembalian: Rp 6.037

Apakah mau bertransaksi lagi? (y/n): n


🚀 Cara Menjalankan

1. Clone repo ini:
git clone https://github.com/dindabelasafitri/diskon_belanja.git
cd diskon_belanja.py

2. Jalankan program:
kasir_sederhana_member.py

🎯 Tujuan Belajar

Latihan Python dasar hingga menengah: input/output, loop, kondisi, list, dictionary

Latihan perhitungan diskon, pajak, dan kembalian

Mengelola data barang per kategori

Membangun logika transaksi multi-step (looping transaksi)
