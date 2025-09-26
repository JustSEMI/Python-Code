'''[ Acara 10 - Perulangan ]'''

# WHILE LOOP
# jumlah = 1
# while jumlah <= 5:
#     print(jumlah)
#     jumlah = jumlah + 1
# print("PROGRAM SELESAI")

# jumlah = 5
# while jumlah > 0:
#     print(jumlah)
#     jumlah -= 1 #sama dengan jumlha = jumlah - 1
# print("PROGRAM SELESAI")

# angka = 0
# while True :
#     print(angka)
#     angka = angka + 1
#     if angka > 5:
#         print("BREAK")
#         break
# print("PROGRAM SELESAI")

# angka = 0
# while True :
#     print(angka)
#     angka = angka + 1
#     if angka == 2:
#         print("SKIP 2")
#         continue
#     if angka == 5:
#         print("BREAK")
#         break
# print("PROGRAM SELESAI")


# FOR LOOP
# BanyakPerulangan = 10
# for index in range(BanyakPerulangan):
#     print("Perulangan ke -", index)

# angka = [1, 7, 3, 5, 9]
# for i in angka:
#     print(i)

# buah = ["nanas", "apel", "jeruk", "mangga", "rambutan"]
# for makanan in buah:
#     print("Saya suka makan", makanan)

# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# jumlah = 0
# for i in angka:
#     jumlah = jumlah + i
# print("Jumlah dari ke 10 bilangan di atas adalah", jumlah)


#NESTED LOOP
# for i in range(3):
#     print('Perulangan luar [i] = ', i)
#     for j in range(5):
#         print('    Perulangan dalam [i, j] = ',i,',')

# for baris in range(5):
#     for kolom in range(7):
#         print('o', end=' ')
#     else:
#         print('')

# i = 6
# while (i > 0):
#     j = 6
#     while (j > i):
#         print('*', end=' ')
#         j -= 1
#     i -= 1
#     print()