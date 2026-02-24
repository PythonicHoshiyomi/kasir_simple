from modules.inputUser import input_semua_barang, input_satu_barang
banyak = int(input("Masukkan jumlah barang yang ingin diinput: "))
semua_barang = input_semua_barang(banyak)

print(semua_barang)

# for barang in semua_barang:
#     print("Nama Barang:", barang["nama"])
#     print("Harga Barang:", barang["harga"])
#     print("Jumlah Barang:", barang["jumlah"])
#     print("--------------------------------")