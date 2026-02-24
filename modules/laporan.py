def printLaporan(data):
    """Cetak laporan penjualan.

    Args:
        data (list of dict): Setiap elemen berisi kunci 'nama', 'harga', dan 'jumlah'.

    Fungsi ini akan menampilkan subtotal per produk, total, dan total akhir.
    """
    if not isinstance(data, list):
        raise ValueError("Data harus berupa list of dict")

    total = 0.0
    print("LAPORAN PENJUALAN")
    print("----------------------------------------")
    print(f"{'Nama':<20}{'Harga':>8}{'Jumlah':>8}{'Subtotal':>12}")
    print("----------------------------------------")
    for item in data:
        nama = item.get('nama', '')
        harga = float(item.get('harga', 0))
        jumlah = int(item.get('jumlah', 0))
        subtotal = harga * jumlah
        total += subtotal
        print(f"{nama:<20}{harga:>8.2f}{jumlah:>8d}{subtotal:>12.2f}")

    print("----------------------------------------")
    print(f"{'Total penjualan:':<30}{total:>18.2f}")
