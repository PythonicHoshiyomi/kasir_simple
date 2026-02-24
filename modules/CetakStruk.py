def CetakStruk(n, semua_barang, total_harga):
    """Cetak daftar barang dan total belanja user."""
    print("Barang yang Anda Beli Adalah")

    for i in range(n):
        barang = semua_barang[i]
        print("Nama Barang:", barang["nama"])
        print("Harga:", barang["harga"])
        print("Jumlah:", barang["jumlah"])
        

    print("Total Harga:", total_harga)





