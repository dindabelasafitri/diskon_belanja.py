# kasir_python.git
Mini project Python: program kasir sederhana dengan perhitungan diskon otomatis.

# kasir sederhana update
Project ini adalah mini project Python untuk mencatat belanjaan, menghitung diskon tiap barang, pajak, diskon member, menampilkan struk rapi, dan mendukung transaksi berulang. Cocok untuk latihan logika pemrograman, list, dictionary, loop, dan perhitungan sederhana.


---

✨ Fitur Utama

Input barang: nama, harga satuan, jumlah beli, diskon (%), kategori.

Hitung otomatis:

Total harga per barang

Diskon tiap barang

Pajak 10% dari total belanja

Diskon tambahan 5% untuk kartu member


Menampilkan struk belanja rapi di layar (dengan timestamp transaksi)

Menampilkan total per kategori dan daftar barang per kategori

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


4. Menampilkan struk belanja dengan timestamp transaksi.


5. Menampilkan daftar barang dan total harga per kategori.


6. Masukkan jumlah pembayaran → program akan menghitung kembalian atau memberi pesan jika uang tidak cukup.


7. Program menanyakan apakah ingin melakukan transaksi baru. Jika ya, loop kembali ke input barang; jika tidak, program selesai.

8. 📂 Struktur Data Barang

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

⚡ Contoh Output

==== DATA BARANG ====
Nama: Indomie
Harga Satuan: Rp 3.000
Jumlah: 5
Total Harga: Rp 15.000
Diskon: 10%
Harga Setelah Diskon: Rp 13.500
Kategori: Makanan
------------------------
Nama: Teh
Harga Satuan: Rp 2.000
Jumlah: 10
Total Harga: Rp 20.000
Diskon: 5%
Harga Setelah Diskon: Rp 19.000
Kategori: Minuman
------------------------

==== STRUK BELANJA ====
Waktu transaksi: 11-09-2025 14:30:25
Total belanja: Rp 32.500
Jumlah diskon: Rp 3.500
Total setelah diskon: Rp 32.500
Total setelah pajak 10%: Rp 35.750
Diskon member: Rp 1.787
Total setelah diskon member: Rp 33.963

=== BARANG BERDASARKAN KATEGORI ===
Makanan: Indomie, total perkategori: Rp 13.500
Minuman: Teh, total perkategori: Rp 19.000

Masukkan jumlah pembayaran: 40000
Total kembalian: Rp 6.037

Apakah anda mau bertransaksi lagi? (y/n): n

🚀 Cara Menjalankan

1. Clone repo ini:

git clone https://github.com/dindabelasafitri/diskon_belanja.git
cd diskon_belanja.py

2. Jalankan program:
   
python kasir_sederhana_timestamp.py

4. Ikuti instruksi input barang, kartu member, dan pembayaran.

🎯 Tujuan Belajar

Latihan Python dasar hingga menengah: input/output, loop, kondisi, list, dictionary

Latihan perhitungan diskon, pajak, kembalian, dan total per kategori

Latihan struk rapi & timestamp transaksi

Membuat multi-transaksi loop, logika program lebih kompleks namun tetap sederhana
