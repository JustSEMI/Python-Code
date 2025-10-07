# 1. buat sebuah set, tampilkan isinya satu persatu.
# 2. buat nested set, tampilkan isinya satu persatu.

jurusan_polije = {'TEKNOLOGI INFORMASI', 'BKP', 'TEKNIK', 'TEKNOLOGI PERTANIAN', 'BISNIS', }
print("SET:")
for jurusan in jurusan_polije:
    print(jurusan)

print()

nested_jurusan_polije = {3.8, 8,'TEKNOLOGI INFORMASI', ('TEKNIK KOMPUTER ', 'TEKNOLOGI INFORMATIKA', 'MANAGEMENT INFORMATIKA', 'TRK'), 'D3', ('D4')}
print("NESTED SET:")
for jurusan_nested in nested_jurusan_polije:
    print(jurusan_nested)



