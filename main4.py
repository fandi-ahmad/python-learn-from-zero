# import datetime as dt

# hari_ini = dt.date.today()

# print(hari_ini)
# # print(f'hari ini adalah, hari {hari_ini:%A}')

# tgl = dt.date(2002,12,19)
# print(tgl)
# # print(f'hari ini adalah, hari {tgl:%A}')
# tanggal = int(input('tanggal \t:'))
# bulan = int(input('bulan \t\t:'))
# tahun = int(input('tahun \t\t:'))
# tanggal_lahir = dt.date(tahun, bulan, tanggal)
# print(tanggal_lahir)


# IF ELSE
# nama = input('siapa nama anda? ')

# 1.
# if nama == 'fandi' : print('benar')

# 2.
# if nama == 'fandi':
#     print('benar')
#     print(f'hai {nama}')
# print('selesai')

# 3.
# if nama == 'fandi':
#     print(f'benar, haii {nama}')
# elif nama == 'faiz':
#     print(f'benar, haii {nama}')
# else:
#     print('salah')


# SIMPLE KALKULATOR
# angka1 = int(input())
# op = input('operator (+,-,*,/)')
# angka2 = int(input())

# if op == "+":
#     print(angka1 + angka2)
# elif op == '-':
#     print(angka1 - angka2)
# elif op == '*':
#     print(angka1 * angka2)
# elif op == '/':
#     print(angka1 / angka2)
# else:
#     print('upps ada yang salah...')


# LOOP
# angka = [0, 2, 4, 6, 8]

# for i in range(5):
#     print(f'i = {i}')

# print('==========')

# angka_range = range(6)
# for i in angka_range:
#     print(f'i = {i}')

# print('==========')

# for i in angka:
#     print(f'i = {i}')

# data = 'ada apa hari ini?'
# for a in data:
#     print(a)


# ===== WHILE LOOP =====
# angka = 0

# while angka < 5:
#     angka+=1
#     print(f'angka = {angka}')


# ===== CONTINUE, PASS, BREAK =====
# pass = tidak dijalanakn (di JS, null)

# angka = 0
# while angka < 5:
#     angka+=1
#     if angka == 3:
#         print('nice lahh')
#         continue
#     print(f'angka = {angka}')

# print('===========')

# angka = 0
# while angka < 5:
#     angka+=1
#     if angka == 3:
#         print('nice lahh')
#         pass
#     print(f'angka = {angka}')

# angka = 0
# while angka < 5:
#     angka+=1
#     print(f'angka = {angka}')
#     if angka == 3:
#         print('nice lahh')
#         break # di selesaikan
#     print('lanjut')
# print('selesai')


# ===== LIST =====

data1 = ['fandi', 'faiz', 'rani']
data2 = ['fitrah', 'fian', 'ozi']

print(data1)
data1.append('ahmad')           # menambahkan diakhir
data1.insert(0, 'bambang')      # menambahkan di awal
data1.extend(data2)             # menggabungkan dengan data2 di akhir
print(data1)
print(data1[3])
data1[0] = 'endi'               # mengganti value data1 untuk index 0
print(data1)

data1.remove('fian')            # hapus data1 sesuai value
data1.remove(data1[0])          # hapus data1 yang di awal
print(data1)
data1.pop()                     # hapus data1 yang di akhir
print(data1)

data_end = data1.pop()
print(data_end)