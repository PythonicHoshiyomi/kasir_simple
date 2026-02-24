PAJAK = 0.13

# total doang
def hitung_total(data_barang):
    total = 0
    for barang in data_barang:
        subtotal = barang["harga"] * barang["jumlah"]
        total += subtotal
    return total

# total + pajak
def hitung_total_akhir(data_barang):
    total = hitung_total(data_barang)
    pajak = total * PAJAK
    total_akhir = total + pajak
    return total, pajak, total_akhir