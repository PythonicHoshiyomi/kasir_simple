from modules.inputUser import input_semua_barang, input_satu_barang
banyak = int(input("Masukkan jumlah barang yang ingin diinput: "))
semua_barang = input_semua_barang(banyak)

print(semua_barang)

# for barang in semua_barang:
#     print("Nama Barang:", barang["nama"])
#     print("Harga Barang:", barang["harga"])
#     print("Jumlah Barang:", barang["jumlah"])
#     print("--------------------------------")
from modules.storage import load_data, save_data

# Load data awal
data = load_data()
print("Data awal:", data)

# Tambah transaksi contoh
transaksi_baru = {
    "nama_barang": "Pulpen",
    "harga": 5000,
    "jumlah": 2,
    "total": 10000
}

data.append(transaksi_baru)

# Simpan ke file
save_data(data)

print("Data berhasil disimpan!")
