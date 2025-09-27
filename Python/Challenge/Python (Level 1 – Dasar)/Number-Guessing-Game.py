import random
import sys

random = random.randint(1, 100)

print("SECRET NUMBER GAME")
attempt = 0
jawaban = int(input("Masukan Tebakaan anda (1-100): "))

while jawaban != random:
    if jawaban < random:
        print("Terlalu Kecil!")
        attempt += 1
        jawaban = int(input("Masukan Tebakaan anda lagi: "))
    elif jawaban > random:
        print("Terlalu Besar!")
        attempt += 1
        jawaban = int(input("Masukan Tebakaan anda lagi: "))
    if attempt == 10:
        print("Game Over!")
    elif jawaban == random:
        print("Tebakan anda Benar! dengan,", attempt, "Percobaan")
        sys.exit()