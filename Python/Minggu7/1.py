#membuat list kosong
listKosong  = []

#memebuat list berisi 1 item
listSatuItem = ['satuItem']

#membuat list dengan banyak item dengan satu tipe data
listKata = ["mangga", "jambu", "apel", "anggur"]
listAngka = [23, 11, 94]

#membuat list dengan berbagai tipe data
listMix = [23, "November", 94]

#mmebuat list berisi list (list bersarang)
listNested = ["Mahasiswa", ["Dian", 17, 160.5], "Lulus"]
listGabungan = [listKata, listAngka]

#mencetak List
print("List Kosong:", listKosong)
print("List Satu Item:", listSatuItem)
print("List Kata:", listKata)
print("List Angka:", listAngka)
print("List Mix:", listMix)
print("List Nested:", listNested)
print("List Gabungan:", listGabungan)

#mencetak index dari list
print(listKata[0])
print(listKata[1])
print(listKata[2])
print(listKata[3])

#mencetak index dari list
print(listKata[-0])
print(listKata[-1])
print(listKata[-2])
print(listKata[-3])
print(listKata[-4])

# mencetak index dari list
print(listNested[0])
print(listNested[1])
print(listNested[1][0])
print(listNested[1][1])
print(listNested[1][2])
print(listNested[2])

# membuat list kosong
listKosong = []
contohKata = "workshop"
contohAngka = 12345678
print(contohKata[5])
print(contohAngka[5])