'''[ Acara 7 - Input dan Output ]'''

#nama = input("Masukkan nama Anda: ")
#usia = input("Masukkan usia Anda: ")
#
#print("Selamat datang, ", nama, ". Anda berusia", usia, "tahun.")

#angka = input("masukan sebuah angka : ")
#print(n+10)

#nama = input("inputkan nama : ")
#usia = int(input("inputkan usia : "))
#tinggi = float(input("inputkan tinggi : "))
#
#print("Hello %s, saat ini usiamu %i tahun dan tinggi badanmu %.2f cm" % (nama, usia, tinggi))

#print(1, 3, 5, 7)
#
#print(1 ,2 ,3 ,4 , sep='*')
#
#print(1,2,3,4, sep='#', end='&')


'''[ Acara 8 - Exception Handling ] '''

#print(x)

#try:
#    print(x)
#except:
#    print("An exception occurred")

#try:
#    angka1 = 9
#    angka2 = 0
#
#    print("angka pertama adalah : ", angka1)
#    print("angka kedua adalah : ", angka2)
#    print(angka1, " bibagi dengan ", angka2, " adalah ", angka1/angka2)
#except ZeroDivisionError:
#    print("Semua bilangan tidak dapat dibagi dengan nol.")

#try:
#    print(x)
#except NameError:
#    print("Variabel x is not defined.")
#except:
#    print("Something went wrong.")

#try:
#    angka1 = 9
#
#    print(angka1 + "buah")
#
#except ZeroDivisionError:
#    print("Terjadi pembagian dengan 0.")
#except (ValueError, TypeError):
#    print("Terjadi error pada value atau tipe.")

#try:
#    print("Hello")
#except:
#    print("Something went wrong")
#else:
#    print("Nothing went wrong")

#try:
#    print(x)
#except:
#    print("Something went wrong")
#finally:
#    print("The 'Try except' is finished")

#try:
#        bagi = 8 / 0
#
#        print(bagi)
#except ZeroDivisionError:
#        print("Tidak bisa membagi dengan nol.")
#
#finally:
#        print("block finally tetap dieksekusi")

#x = -1
#
#if x < 0:
#    raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")