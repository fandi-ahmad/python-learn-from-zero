# # ===== LIST =====
# data_angka = [1,2,4,5,7,4,9,4,3,8]
# jumlah = len(data_angka)
# print(data_angka)

# angka_4 = data_angka.count(4)
# print(angka_4)

# data1 = ['fandi', 'faiz', 'rani']

# data_angka.sort()   # diurutkan dari 0
# print(data_angka)

# print(data1)

# data1.sort()    # diurutkan dari a-z
# print(data1)

# data_angka.reverse()    # membalikan urutan
# data1.reverse()

# print(data_angka)
# print(data1)


# # ===== COPY LIST =====
# data1 = ['fandi', 'faiz', 'rani']

# data2 = data1           # data2 adalah data1 yang saling terhubung
# data3 = data1.copy()    # data3 adalah data baru dan salinan data1 saat ini
# data1[0] = 'endi'
# data3[2] = 'toto'

# print(data1)
# print(data2)
# print(data3)


# # ===== NESTED LIST =====
# p1 = ['fandi', 20, 'laki-laki']
# p2 = ['faiz', 17, 'laki-laki']
# p3 = ['rani', 6, 'perempuan']

# list_peserta = [p1, p2, p3]
# print(list_peserta)

# for p in list_peserta:
#     print(f'nama\t: {p[0]}')
#     print(f'umur\t: {p[1]}')
#     print(f'gender\t: {p[2]}\n')


# # ===== LOOPING LIST =====
# angkas = [4,3,2,5,6,1]

# # for angka in angkas:
# #     print(f'angka = {angka}')

# peserta = ['fandi', 'faiz', 'rani']
# # for nama in peserta:
# #     print(f'nama = {nama}')

# for index, data in enumerate(peserta):
#     print(f'{index+1}. {data}')


# # ===== LATIHAN LIST BUKU =====
# list_buku = []
# while True:
#     print('masukan data buku')
#     judul = input('judul buku : ')
#     penulis = input('nama penulis : ')

#     buku_baru = [judul, penulis]
#     list_buku.append(buku_baru)

#     for index, buku in enumerate(list_buku):
#         print(f'{index+1} | {buku[0]} | {buku[1]}')
    
#     isNext = input('apakah masihh lanjut? (y/n) ')
#     if isNext == 'n':
#         break


# ===== DICTIONARY =====
# data_dict = {
#     'key': 'value',
#     'fn': 'fandi',
#     'fz': 'faiz',
#     'ra': 'rani'
# }

# print(data_dict)
# print(data_dict['fn'])
# print(data_dict.get('ra'))
# print(data_dict.get('fz', 'tidak ada'))     # 'tidak ada' adalah pesan jika key tidak ditemukan

# data_dict['ri'] = 'rizki'
# print(data_dict)

# data_dict.update({'fn': 'fandi ahmad'})     # jika key nya ada/sama maka diupdate, jika tidak maka ditambah
# print(data_dict)
# data_dict.update({'ft': 'fitrah'})
# print(data_dict)

# del data_dict['key']                        # delete
# print(data_dict)

# for nama in data_dict:
#     print(nama)

# keys = data_dict.keys()


# values = data_dict.values()
# print(values)

# for v in values:
#     print(v)

# items = data_dict.items()
# print(items)


# ===== COPY DICTIONARY =====
semua_teman = {
    'fn': 'fandi',
    'fz': 'faiz',
    'ra': 'rani',
    'rz': 'rizki',
    'sp': 'septian'
}

friends = semua_teman.copy()    # copy

print(semua_teman)
print(friends)

semua_teman['fz'] = 'fikar'     # update/replace dari key
print('=============')
print(semua_teman)
print(friends)

# ===== POP DICTIONARY =====
dataRani = friends.pop('ra')    # mengambil data dari key
print('=============')
print(semua_teman)
print(friends)
print(dataRani)

dataEnd = friends.popitem()     # mengambil data terakhir
print('=============')
print(semua_teman)
print(friends)
print(dataEnd)

