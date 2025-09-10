def format_rp(nilai):
    return f"Rp {nilai:,.0f}".replace(",", ".")

daftar_belanja = []
while True:
    nama_barang = input("Masukkan nama barang: ")
    while True:
        try:
            harga_asli = int(input("Masukkan harga barang: "))
            diskon_persen = int(input("Masukkan diskon(%): "))
            break
        except ValueError:
            print("Harga dan diskon harus berupa angka!")

    potongan_diskon = harga_asli * diskon_persen / 100
    harga_final = harga_asli - potongan_diskon

    data = {
        "nama": nama_barang,
        "harga_asli": harga_asli,
        "diskon_persen": diskon_persen,
        "potongan_diskon": potongan_diskon,
        "harga_final": harga_final
    }
    daftar_belanja.append(data)

    lanjut = input("Mau nambah barang? (y/n): ")
    if lanjut.lower() != "y":
        break

# Hitung total
total_belanja = sum(item["harga_final"] for item in daftar_belanja)
total_diskon = sum(item["potongan_diskon"] for item in daftar_belanja)
pajak = total_belanja * 0.10
total_bayar = total_belanja + pajak

# Cetak struk
print("\nData Barang")
for item in daftar_belanja:
    print(f"Nama: {item['nama']}, Harga: {format_rp(item['harga_asli'])}, "
          f"Diskon: {item['diskon_persen']}%, "
          f"Harga setelah diskon: {format_rp(item['harga_final'])}")

print("\n=== STRUK BELANJA ===")
print(f"Total belanja: {format_rp(total_belanja)}")
print(f"Jumlah diskon: {format_rp(total_diskon)}")
print(f"Pajak (10%): {format_rp(pajak)}")
print(f"Total bayar: {format_rp(total_bayar)}")

# Input pembayaran
while True:
    try:
        pembayaran = int(input("Masukkan jumlah pembayaran: "))
        break
    except ValueError:
        print("Harus angka!")

if pembayaran > total_bayar:
    print(f"Total kembalian: {format_rp(pembayaran - total_bayar)}")
elif pembayaran == total_bayar:
    print("Pembayaran pas, terima kasih!")
else:
    print("Jumlah pembayaran tidak cukup!")
