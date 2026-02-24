from modules.inputUser import input_semua_barang
from modules.laporan import printLaporan
from modules.storage import load_data, save_data
from modules.CetakStruk import CetakStruk
from modules.HitungTotal import hitung_total_akhir, PAJAK


def tampilkan_menu():
    """Tampilkan menu utama aplikasi."""
    print("\n" + "="*50)
    print("APLIKASI KASIR SEDERHANA".center(50))
    print("="*50)
    print("\n1. Input Barang Baru")
    print("2. Cetak Struk Transaksi")
    print("3. Lihat Laporan Penjualan")
    print("4. Lihat Riwayat Semua Transaksi")
    print("5. Keluar")
    print("\n" + "-"*50)


def input_barang():
    """Menu untuk input barang."""
    print("\n[INPUT BARANG BARU]")
    try:
        banyak = int(input("Masukkan jumlah barang: "))
        if banyak <= 0:
            print("[ERROR] Jumlah barang harus lebih dari 0.")
            return
        
        semua_barang = input_semua_barang(banyak)
        
        # Tampilkan struk
        CetakStruk(semua_barang)
        
        # Tanyakan apakah ingin disimpan
        simpan = input("Simpan transaksi ke riwayat? (y/n): ").lower()
        if simpan == 'y':
            save_data(semua_barang)
            print("[OK] Data berhasil disimpan ke riwayat.json")
        else:
            print("[SKIP] Data tidak disimpan.")
    except ValueError:
        print("[ERROR] Input tidak valid. Masukkan angka.")


def lihat_laporan():
    """Menu untuk lihat laporan."""
    print("\n[LAPORAN PENJUALAN]")
    riwayat = load_data()
    
    if not riwayat:
        print("[WARNING] Tidak ada data transaksi.")
        return
    
    # Jika riwayat berisi list of transactions
    semua_item = []
    for transaksi in riwayat:
        if isinstance(transaksi, list):
            semua_item.extend(transaksi)
        else:
            semua_item.append(transaksi)
    
    if semua_item:
        printLaporan(semua_item)
    else:
        print("[WARNING] Tidak ada data item untuk ditampilkan.")


def lihat_riwayat():
    """Menu untuk lihat riwayat transaksi."""
    print("\n[RIWAYAT TRANSAKSI]")
    riwayat = load_data()
    
    if not riwayat:
        print("[WARNING] Tidak ada riwayat transaksi.")
        return
    
    print(f"\nTotal transaksi: {len(riwayat)}\n")
    print("="*80)
    
    for idx, transaksi in enumerate(riwayat, 1):
        print(f"\nTransaksi #{idx}:")
        print("-" * 80)
        
        if isinstance(transaksi, list):
            # Jika transaksi adalah list barang
            total, pajak, total_akhir = hitung_total_akhir(transaksi)
            for item in transaksi:
                print(f"  • {item.get('nama', 'N/A'):<20} "
                      f"Harga: Rp {item.get('harga', 0):>10,.2f} | "
                      f"Qty: {item.get('jumlah', 0):>3d} | "
                      f"Tanggal: {item.get('tanggal_pembelian', 'N/A')}")
            print(f"\n  Total Sebelum Pajak: Rp {total:>10,.2f}")
            print(f"  Pajak ({int(PAJAK*100)}%):             Rp {pajak:>10,.2f}")
            print(f"  Total Akhir:         Rp {total_akhir:>10,.2f}")
        else:
            # Jika transaksi adalah dict barang tunggal
            print(f"  Nama: {transaksi.get('nama', 'N/A')}")
            print(f"  Harga: Rp {transaksi.get('harga', 0):,.2f}")
            print(f"  Jumlah: {transaksi.get('jumlah', 0)}")
            print(f"  Tanggal: {transaksi.get('tanggal_pembelian', 'N/A')}")
    
    print("\n" + "="*80)


def main():
    """Fungsi utama aplikasi."""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == '1':
            input_barang()
        elif pilihan == '2':
            print("\n[CETAK STRUK TRANSAKSI]")
            try:
                banyak = int(input("Masukkan jumlah barang: "))
                if banyak <= 0:
                    print("[ERROR] Jumlah barang harus lebih dari 0.")
                    continue
                semua_barang = input_semua_barang(banyak)
                CetakStruk(semua_barang)
            except ValueError:
                print("[ERROR] Input tidak valid.")
        elif pilihan == '3':
            lihat_laporan()
        elif pilihan == '4':
            lihat_riwayat()
        elif pilihan == '5':
            print("\n[EXIT] Terima kasih telah menggunakan aplikasi kasir.")
            print("Sampai jumpa!\n")
            break
        else:
            print("[ERROR] Pilihan tidak valid. Silakan pilih 1-5.")


if __name__ == '__main__':
    main()
