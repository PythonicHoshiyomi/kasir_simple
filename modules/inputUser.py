from datetime import datetime

def input_satu_barang():
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = float(input("Masukkan harga barang: "))
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    tanggal_pembelian = datetime.now().strftime("%Y-%m-%d")
    return {"nama": nama_barang, "harga": harga_barang, "jumlah": jumlah_barang, "tanggal_pembelian": tanggal_pembelian}
        
def input_semua_barang(banyak):

    data = []
    
    for i in range(banyak):
        print(f"\nBarang ke-{i+1}:")
        barang = input_satu_barang()
        data.append(barang)
        
    return data