# listKata = ['mangga','jambu','apel','anggur']
# print(listKata[0:1])
# print(listKata[0:2])
# print(listKata[1:3])
# print(listKata[0:-1])
# print(listKata[-1:-3])
# print(listKata[-1:3])
# print(listKata[-3:-1])

# asd = ['nol','satu','dua','tiga','empat','mintiga','mindua','minsatu']
# print(asd[1:3])
# print(asd[0:-1])
# print(asd[-1:-3])
# print(asd[-1:3])
# print(asd[-3:-1])
# print(asd[-4:-1])
# print(asd[-4:-2])

# listKata = ["mangga", "jambu", "apel", "anggur"]
# print(listKata [0:])
# print(listKata [1:])
# print(listKata [2:])
# print(listKata [3:])
# print(listKata[:0])
# print(listKata[:1])
# print(listKata[:2])
# print(listKata[:3])
# print(listKata[:4])
# print()
# print(listKata [-1:])
# print(listKata[-2:])
# print(listKata [-3:])
# print(listKata[:0])
# print(listKata[:-1])
# print(listKata[:-2])
# print(listKata[:-3])
# print(listKata[:-4])

# listKata = ["mangga", "jambu", "apel", "anggur"]
# print(listKata)
# # Mengubah indeks ke 1 pada listKata
# print("Sesudah indeks ke 1 diubah :')")
# listKata[1] = "rambutan"
# print(listKata)
# # Menambah list pada listKata tetapi tidak disimpan
# print("List juga bisa ditambahkan :')")
# print(listKata+["delima", "melon", "pear"])
# # Menambah list pada listKata lalu disimpan
# print("List juga bisa ditambahkan kemudian disimpan :')")
# listKata = listKata+["delima", "melon", "pear"]
# print(listKata)
# # Mengalikan list pada listKata
# print("List juga bisa dikalikan :')")
# print(listKata*2)
# # Memeriksa item dalam list
# print("mangga" in listKata)
# print("salak" not in listKata)
# if "melon" in listKata:
#     print("ada melon di dalam listKata")

# nomor = [1, 5, 7, 9, 11]
# # mendapatkan jumlah item pada list menggunakan len
# print('menghitung jumlah item pada list:')
# print(len(nomor))
# # menambahkan item di akhir list menggunakan append
# print('menambah angka 13 menggunakan append:')
# nomor.append(13)
# print(nomor)
# # menyisipkan item pada indeks tertentu menggunakan insert
# print('menyisipkan angka 3 pada indeks ke-1 menggunakan insert :')
# indeks = 1
# nomor.insert(indeks, 3)
# print(nomor)
# # menambah list pada list menggunakan extend
# print('menambah list berisi 15, 17, 19 pada list nomor :')
# nomor.extend([15, 17, 19])
# print(nomor)
# # cek indeks ke berapa
# print('cek angka 1 di indeks keberapa? angka 2 di indeks keberapa?')
# print(nomor.index(1))
# print(nomor.index(2))

# listHari = ['hari', 'senin', 'selasa', 'maret', 'rabu', 'kamis', 'juni']
# print(listHari)
# # remove = menghapus nilai yang sama
# print('menghapus maret dari list :')
# listHari.remove('maret')
# print(listHari)
# # kata kunci del = menghapus nilai item sesuai dengan indeks yang diminta
# print('menghapus indeks ke 0 yaitu hari :')
# del listHari[0]
# print(listHari)
# # pop = menghapus nilai item sesuai dengan indeks yang diminta
# print('menghapus indeks ke 4 yaitu juni menggunakan pop :')
# listHari.pop(4)
# print(listHari)
# # pop = menghapus nilai item terakhir pada list yaitu kamis
# print('menghapus indeks terakhir (kamis) menggunakan pop :')
# listHari.pop()
# print(listHari)
# # mencetak nilai yang dihapus menggunakan pop
# print('mencetak nilai yang dihapus pop pada indeks ke 0 yaitu senin :')
# print(listHari.pop(0))

# listAngka = [3, 5, 8, 1, 2, 9, 7, 4, 6,]
# listHuruf = ['doni','caca','eva','bobi,','ani','faruk']
# print(listAngka)
# print(listHuruf)
# # mengurutkan isi list berupa angka dan kata menggunakan sort
# print('marilah kita urutkan :')
# listAngka.sort()
# listHuruf.sort()
# print(listAngka)
# print(listHuruf)
# # membalik index isi list berapa angka dan kata menggunakan reverse
# print('membalik urutan index :')
# listAngka.reverse()
# listHuruf.reverse()
# print(listAngka)
# print(listHuruf)

#list minuman dengan 2 dimensi
list_minuman = [
    ["kopi","susu","teh"],
    ["jus apel","jus melon","jur jeruk"],
    ["es kopi","es campur","es teler"]
]
print(list_minuman)
print('\n')
# cara mengakses list multidiemnsi
# angka pertama menunjukkan kolom,yang kedua adalah baris
print("menampilkan salah satu menu dengan menunjuk nomer index :")
print(list_minuman[2][0])
print(list_minuman[0][1])
print('\n')
# mencetak isi list di dalam list satu persatu
print('\n')
print("menampilkan isi list di dalam list :")
for menu in list_minuman:
    for menu2 in menu:
        print(menu2)