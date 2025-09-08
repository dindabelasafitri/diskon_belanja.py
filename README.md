# diskon_belanja.py
Mini project Python: program kasir sederhana dengan perhitungan diskon otomatis.

# Kasir Sederhana Update

Program ini adalah **mini project Python** untuk mencatat belanjaan, menghitung total harga dengan diskon otomatis, dan menghitung kembalian setelah pembayaran. Cocok sebagai latihan **Python dasar dan logika pemrograman**.

## Fitur
- Input nama dan harga barang (angka saja, tanpa titik)
- Menyimpan semua barang yang valid ke struk
- Menghitung total belanja
- Menghitung diskon otomatis:
  - Total >= 200.000 → diskon 15%
  - Total >= 100.000 → diskon 10%
  - Total < 100.000 → tidak ada diskon
- Menampilkan struk belanja lengkap
- Input pembayaran dan menghitung kembalian
- Memberi pesan jika jumlah uang pembayaran tidak cukup

## Cara Pakai
1. Jalankan program:
```bash
python kasir_sederhana_diskon.py

2. Masukkan nama barang dan harga.
⚠️ Catatan: harga harus berupa angka langsung, misal 15000, jangan pakai titik.


3. Program akan menampilkan struk belanja, total belanja, diskon (jika ada), dan total akhir.


4. Masukkan jumlah uang pembayaran untuk menghitung kembalian.


Contoh Output

=== STRUK BELANJA ===
Buku: 50000
Pulpen: 10000
Tas: 120000

Total sebelum diskon: 180000
Diskon: 18000
Total setelah diskon: 162000

Masukkan jumlah uang pembayaran: 200000
Jumlah kembalian: 38000

Author
Dinda Bela Safitri

Catatan

Project ini merupakan versi final dari mini project kasir sebelumnya dengan penambahan fitur pembayaran dan kembalian. Semua susunan dan logika program dibuat sendiri sebagai latihan Python.

