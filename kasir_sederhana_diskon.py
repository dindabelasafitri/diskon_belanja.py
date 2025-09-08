# kasir_sederhana_diskon.py

struk_barang = []

# input barang
while True:
    nama = input("Masukkan nama barang: ")

    while True:
        harga_input = input("Masukkan harga barang: ")
        try:
            harga = int(harga_input)
            break
        except ValueError:
            print("Harga harus angka!")

    data_barang = {"nama": nama, "harga": harga}
    struk_barang.append(data_barang)

    lanjut = input("Mau tambah barang? (y/n): ")
    if lanjut.lower() != "y":
        break

# menghitung total belanja
total_sebelum_diskon = sum(s["harga"] for s in struk_barang)

# fungsi hitung diskon
def hitung_diskon(total):
    if total >= 200000:
        return total * 0.15  # 15% diskon
    elif total >= 100000:
        return total * 0.10  # 10% diskon
    else:
        return 0

jumlah_diskon = hitung_diskon(total_sebelum_diskon)
total_setelah_diskon = total_sebelum_diskon - jumlah_diskon

# menampilkan struk
print("\n=== STRUK BELANJA ===")
for s in struk_barang:
    print(f"{s['nama']}: {s['harga']}")

print(f"\nTotal sebelum diskon: {total_sebelum_diskon}")
if jumlah_diskon > 0:
    print(f"Diskon: {jumlah_diskon}")
else:
    print("Diskon: 0")
print(f"Total setelah diskon: {total_setelah_diskon}")

# input pembayaran
while True:
    try:
        jumlah_uang = int(input("Masukkan jumlah uang pembayaran: "))
        break
    except ValueError:
        print("Harus angka!")

# hitung kembalian
if jumlah_uang >= total_setelah_diskon:
    kembalian = jumlah_uang - total_setelah_diskon
    print(f"Jumlah kembalian: {kembalian}")
else:
    print("Jumlah uang tidak cukup!")
