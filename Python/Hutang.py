hutang = float(input("Jumlah Hutang: "))
persen_bunga = float(input("Jumlah Bunga Hutang: "))
jumlah_hari = int(input("Jumlah Hari: "))

hutang_akhir = hutang * (1 + (persen_bunga / 100)) ** jumlah_hari

print("Hutang akhir setelah,", jumlah_hari, "hari adalah: Rp.", int(hutang_akhir))