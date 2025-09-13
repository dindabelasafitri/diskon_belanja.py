def format_rp(nilai):
    return f"Rp {nilai:,.0f}".replace(",", ".")

struk_belanja = []
daftar_kategori = {}
while True:
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

           # Hitungan per barang
           total_harga = harga_satuan * jumlah_beli
           total_diskon = total_harga * diskon_persen / 100
           harga_setelah_diskon = total_harga - total_diskon

           # Simpan data barang ke dictionary
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

           # Simpan juga ke daftar kategori
           if kategori_barang not in daftar_kategori:
              daftar_kategori[kategori_barang] = []
           daftar_kategori[kategori_barang].append(data_barang)

           lanjut = input("Mau nambah barang? (y/n): ")
           if lanjut.lower() != "y":
              break

      # Hitungan total keseluruhan
      total_belanja = sum(s["harga_setelah_diskon"] for s in struk_belanja)
      total_semua_diskon = sum(s["total_diskon"] for s in struk_belanja)
      pajak = total_belanja * 0.10
      total_setelah_pajak = total_belanja + pajak

      # Kartu member
      kartu_member = input("Apakah anda punya kartu member? (y/n): ")
      diskon_member = 0
      if kartu_member.lower() == "y":
         diskon_member = total_setelah_pajak * 0.05
         total_setelah_pajak -= diskon_member

      # Tampilkan data barang
      print("\nData Barang")
      for s in struk_belanja:
          print(f"Nama: {s['nama']}, Harga Satuan: {format_rp(s['harga_satuan'])}, Jumlah: {s['jumlah_beli']}, "
          f"Total Harga: {format_rp(s['total_harga'])}, Diskon: {s['diskon_persen']}%, "
          f"Harga Setelah Diskon: {format_rp(s['harga_setelah_diskon'])}, Kategori: {s['kategori']}")

      # Tampilkan struk
      print("\n=== STRUK BELANJA ===")
      print(f"Total belanja: {format_rp(total_belanja)}")
      print(f"Jumlah diskon: {format_rp(total_semua_diskon)}")
      print(f"Total setelah diskon: {format_rp(total_belanja)}")
      print(f"Total setelah pajak 10%: {format_rp(total_belanja + pajak)}")
      if diskon_member > 0:
         print(f"Diskon member: {format_rp(diskon_member)}")
         print(f"Total setelah diskon member: {format_rp(total_setelah_pajak)}")
      else:
         print("Tidak menggunakan kartu member")

      # Tampilkan daftar berdasarkan kategori
      print("\n=== BARANG BERDASARKAN KATEGORI ===")
      for kategori, daftar in daftar_kategori.items():
         daftar_nama = [barang["nama"] for barang in daftar]
         print(f"{kategori.capitalize()}: {', '.join(daftar_nama)}")

      # Input pembayaran
      while True:
            try:
               pembayaran = int(input("Masukkan jumlah pembayaran: "))
               break
            except ValueError:
               print("Harus angka!")

      if pembayaran > total_setelah_pajak:
         print(f"Total kembalian: {format_rp(pembayaran - total_setelah_pajak)}")
      elif pembayaran == total_setelah_pajak:
         print("Pembayaran pas, terima kasih!")
      else:
         print("Jumlah pembayaran tidak cukup!")


      lanjut_transaksi = input("apakah ada mau bertransaksi lagi? (y/n): ")
      if lanjut_transaksi == "y":
         continue
      else:
         break
