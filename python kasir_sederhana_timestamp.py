from datetime import datetime

def format_rp(nilai):
    return f"Rp {nilai:,.0f}".replace(",", ".")

while True:
    struk_belanja = []
    daftar_kategori = {}

    # Input barang
    while True:
        nama_barang = input("Masukkan nama barang: ")
        while True:
            try:
                harga_satuan = int(input("Masukkan harga barang: "))
                diskon_persen = int(input("Masukkan diskon(%): "))
                jumlah_beli = int(input("Masukkan jumlah barang yang dibeli: "))
                kategori_barang = input("Masukkan kategori barang: ")
                break
            except ValueError:
                print("Harga, diskon, dan jumlah harus berupa angka!")

        total_harga = harga_satuan * jumlah_beli
        total_diskon = total_harga * diskon_persen / 100
        harga_setelah_diskon = total_harga - total_diskon

        data_barang = {
            "nama": nama_barang,
            "harga_satuan": harga_satuan,
            "jumlah_beli": jumlah_beli,
            "total_harga": total_harga,
            "diskon_persen": diskon_persen,
            "total_diskon": total_diskon,
            "harga_setelah_diskon": harga_setelah_diskon,
            "kategori": kategori_barang
        }
        struk_belanja.append(data_barang)

        if kategori_barang not in daftar_kategori:
            daftar_kategori[kategori_barang] = []
        daftar_kategori[kategori_barang].append(data_barang)

        lanjut = input("Mau nambah barang? (y/n): ")
        if lanjut.lower() != "y":
            break

    # Hitungan total
    total_belanja = sum(s["harga_setelah_diskon"] for s in struk_belanja)
    total_semua_diskon = sum(s["total_diskon"] for s in struk_belanja)
    pajak = total_belanja * 0.10
    total_setelah_pajak = total_belanja + pajak

    ts = datetime.now().timestamp()
    waktu_readable = datetime.fromtimestamp(ts).strftime("%d-%m-%Y %H:%M:%S")

    kartu_member = input("Apakah anda punya kartu member? (y/n): ")
    diskon_member = 0
    if kartu_member.lower() == "y":
        diskon_member = total_setelah_pajak * 0.05
        total_setelah_pajak -= diskon_member

    # Buat struk teks rapi
    struk_text = "\n==== DATA BARANG ====\n"
    for s in struk_belanja:
        struk_text += (
            f"Nama: {s['nama']}\n"
            f"Harga Satuan: {format_rp(s['harga_satuan'])}\n"
            f"Jumlah: {s['jumlah_beli']}\n"
            f"Total Harga: {format_rp(s['total_harga'])}\n"
            f"Diskon: {s['diskon_persen']}%\n"
            f"Harga Setelah Diskon: {format_rp(s['harga_setelah_diskon'])}\n"
            f"Kategori: {s['kategori']}\n"
            "------------------------\n"
        )

    struk_text += "\n==== STRUK BELANJA ====\n"
    struk_text += f"Waktu transaksi: {waktu_readable}\n"
    struk_text += "----------------------------\n"
    struk_text += f"Total belanja: {format_rp(total_belanja)}\n"
    struk_text += f"Jumlah diskon: {format_rp(total_semua_diskon)}\n"
    struk_text += f"Total setelah diskon: {format_rp(total_belanja)}\n"
    struk_text += f"Total setelah pajak 10%: {format_rp(total_belanja + pajak)}\n"

    if diskon_member > 0:
        struk_text += f"Diskon member: {format_rp(diskon_member)}\n"
        struk_text += f"Total setelah diskon member: {format_rp(total_setelah_pajak)}\n"
    else:
        struk_text += "Tidak menggunakan kartu member\n"
    struk_text += "===============================\n"

    struk_text += "\n=== BARANG BERDASARKAN KATEGORI ===\n"
    for kategori, daftar in daftar_kategori.items():
        daftar_nama = [barang["nama"] for barang in daftar]
        jumlah_harga_kategori = sum(barang["harga_setelah_diskon"] for barang in daftar)
        struk_text += f"{kategori.capitalize()}: {', '.join(daftar_nama)}, total perkategori: {format_rp(jumlah_harga_kategori)}\n"

    while True:
        try:
            pembayaran = int(input("Masukkan jumlah pembayaran: "))
            break
        except ValueError:
            print("Harus angka!")

    if pembayaran > total_setelah_pajak:
        struk_text += f"Total kembalian: {format_rp(pembayaran - total_setelah_pajak)}\n"
    elif pembayaran == total_setelah_pajak:
        struk_text += "Pembayaran pas, terima kasih!\n"
    else:
        struk_text += "Jumlah pembayaran tidak cukup!\n"

    # Print struk di layar Colab (tinggal copy-paste ke Google Docs / Notes di HP)
    print(struk_text)

    lanjut_transaksi = input("Apakah anda mau bertransaksi lagi? (y/n): ")
    if lanjut_transaksi.lower() != "y":
        break
