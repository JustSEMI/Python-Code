import calendar
import sys

# tupleKosong = ()
# tupleSingleton = ('satu')
# tupleSingleton2 = (1,)
# tupleSingleton3 = 'satu',
# tupleBulan = ('januari', 'februari','maret','april','mei','juni')
# # tuple bisa di buat tanpa tanda kurung
# tupleAngka = 1,2,3,4,5,6,7,8,9,10
# print(tupleKosong)
# print(tupleSingleton)
# print(tupleSingleton2)
# print(tupleSingleton3)
# print(tupleBulan)
# print(tupleAngka)
# print('\n')
# # cek tipe data, apakah sudah benar bertipe data tuple
# print(type(tupleSingleton))
# print(type(tupleSingleton2))
# print(type(tupleSingleton3))  
# print(type(tupleAngka))

# tupleKosong = ()
# tupleSingleton = ('satu')
# tupleSingleton2 = (1,)
# tupleSingleton3 = 'satu',
# tupleBulan = ('januari', 'februari','maret','april','mei','juni')
# # tuple bisa di buat tanpa tanda kurung
# tupleAngka = 1,2,3,4,5,6,7,8,9,10
# #menggabungkan 2 tuple jadi satu
# tupleGab = tupleSingleton3 + tupleAngka
# print(tupleGab)
# # mengakses data tuple
# print(tupleBulan[0])
# print(tupleBulan[3])
# print(tupleBulan[5])
# print(tupleBulan[-1])
# print(tupleBulan[-3])
# print(tupleBulan[-5])


# # slicing tuple
# print(tupleAngka[0:3])
# print(tupleAngka[1:-1]) #memotong index ke 1 hinnga -1
# print(tupleAngka[-1:1])
# print('\n')
# # slicing tanpa batas
# print(tupleAngka[2:1])
# print(tupleAngka[5:])
# print(tupleAngka[8:])
# print(tupleAngka[:0])
# print(tupleAngka[:1])
# print(tupleAngka[:3])
# print(tupleAngka[:5])

# # index kelipatan
# # dari index awal hingga akhir, kelipatan index 2 langkah
# print(tupleAngka[:2])
# # dari index 1 hingga ke8, kelipatan index 3 langkah
# print(tupleAngka[1:8:3])

# # mencoba mengubah tuple index ke 0 dari angka 1 menjadi angka 0
# tupleAngka[0] = 0

# tuple1 = (1,2,3)
# tuple2 = ('satu','dua','tiga')
# tuple3 = ('andi',23,68.5)
# tuple4 = tuple1,tuple2,tuple3

# print(tuple1)
# print(tuple2)
# print(tuple3)
# print(tuple4)
# print(tuple4[1][2])
# print(tuple4[2][0])

# nama, usia, berat = tuple3
# print('nama : ',nama)
# print('usia : ',usia)
# print('berat : ',berat)

# tuple1 = (1,2,3)
# tuple2 = ('satu','dua','tiga')
# tuple3 = ('andi',23,68.5)
# tuple4 = tuple1,tuple2,tuple3
# print(max(tuple1))
# print(min(tuple1))
# print(len(tuple1))

tupleBulan = ('januari', 'februari','maret','april','mei','juni','juli','agustus','september','oktober','november','desember')
for month in tupleBulan:
    print(month)