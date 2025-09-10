def format_rp(nilai):
    return f"Rp {nilai:,.0f}".replace(",", ".")

struk_belanja = []
while True:
    nama = input("masukkan nama barang: ")
    while True:
        harga_input = input("masukkan harga barang: ")
        try:
            harga = int(harga_input)
            diskon = int(input("masukkan diskon(%): "))
            jumlah = int(input("masukkan jumlah barang yang di beli: "))
            kategori_barang = input("kategori barang: ")
            break
        except ValueError:
            print("harga dan diskon harus angka!")
            

    jumlah_barang = harga * jumlah
    jumlah_diskon = jumlah_barang * diskon / 100
    setelah_diskon = jumlah_barang - jumlah_diskon
    data_barang = {
        "nama": nama,
        "harga": harga,
        "diskon": diskon,
        "harga_setelah_diskon": setelah_diskon,
        "jumlah_diskon": jumlah_diskon,
        "jumlah_barang": jumlah_barang,
        "kategori": kategori_barang
    }
    struk_belanja.append(data_barang)

    lanjut = input("mau nambah barang?(y/n): ")
    if lanjut.lower() != "y":
        break

total_belanja = sum(s["harga_setelah_diskon"] for s in struk_belanja)
total_diskon = sum(s["jumlah_diskon"] for s in struk_belanja)
potong_pajak = total_belanja * 0.10
total_pajak = total_belanja + potong_pajak

print("\nData Barang")
for s in struk_belanja:
    print(f"Nama: {s['nama']}, Harga: {format_rp(s['harga'])}, Diskon: {s['diskon']}%, harga setelah diskon: {format_rp(s['harga_setelah_diskon'])}, Kategori: {s['kategori']}")

print("\n=== STRUK BELANJA ===")
print(f"Total belanja: {format_rp(total_belanja)}")
print(f"Jumlah diskon: {format_rp(total_diskon)}")
print(f"Total setelah diskon: {format_rp(total_belanja)}")
print(f"Total setelah potong pajak: {format_rp(total_pajak)}")

# Input pembayaran dengan loop agar aman
while True:
    try:
        pembayaran = int(input("Masukkan jumlah pembayaran: "))
        break
    except ValueError:
        print("Harus angka!")

if pembayaran > total_pajak:
    print(f"Total kembalian: {format_rp(pembayaran - total_pajak)}")
elif pembayaran == total_pajak:
    print("Pembayaran pas, terima kasih!")
else:
    print("Jumlah pembayaran tidak cukup!")
