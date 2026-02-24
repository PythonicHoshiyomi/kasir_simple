from modules.HitungTotal import hitung_total_akhir, PAJAK

def CetakStruk(semua_barang):
    """Cetak struk belanja dengan detail barang, subtotal, pajak, dan total.
    
    Parameters
    ----------
    semua_barang : list of dict
        List berisi dict dengan kunci 'nama', 'harga', 'jumlah', 'tanggal_pembelian'.
    """
    if not semua_barang:
        print("Tidak ada barang yang dibeli.")
        return

    print("\n" + "="*50)
    print("STRUK BELANJA".center(50))
    print("="*50)
    
    # Header tabel
    print(f"\n{'No':<4}{'Nama':<18}{'Harga':>8}{'Qty':>4}{'Subtotal':>10}")
    print("-" * 50)
    
    # Detail setiap barang
    for idx, barang in enumerate(semua_barang, 1):
        nama = barang.get('nama', '')
        harga = float(barang.get('harga', 0))
        jumlah = int(barang.get('jumlah', 0))
        subtotal = harga * jumlah
        
        print(f"{idx:<4}{nama:<18}{harga:>8.2f}{jumlah:>4d}{subtotal:>10.2f}")
    
    print("-" * 50)
    
    # Perhitungan total menggunakan HitungTotal
    total, pajak, total_akhir = hitung_total_akhir(semua_barang)
    pajak_persen = int(PAJAK * 100)
    
    print(f"\nTanggal           : {semua_barang[0].get('tanggal_pembelian', 'N/A')}")
    print(f"Total Sebelum Pajak: Rp {total:>10,.2f}")
    print(f"Pajak ({pajak_persen}%)         : Rp {pajak:>10,.2f}")
    print("-" * 50)
    print(f"TOTAL             : Rp {total_akhir:>10,.2f}")
    print("="*50)
    print("Terima kasih telah berbelanja!".center(50))
    print("="*50 + "\n")