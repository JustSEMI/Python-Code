import random
import sys

secret_number = random.randint(1, 100)
attempt = 0
guest = -1

print("SECRET NUMBER GAME")

while guest != secret_number:
    attempt += 1
    guest = int(input("Masukan Tebakaan anda (1-100): "))

    if guest < secret_number:
        print("Tebakan anda terlalu Rendah!!!")
    elif guest > secret_number:
        print("Tebakan anda terlalu Tinggi!!!")
    else:
        print(f"Selamat Tebakan anda benar dalam {attempt} kali percobaan")
    
    if attempt == 7:
        print("GAME OVER")
        break
sys.exit()