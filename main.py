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
