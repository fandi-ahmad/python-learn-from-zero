import datetime
import os
import string
import random

# mhs1 = {
#     'nama': 'fandi ahmad',
#     'nim': '5520120026',
#     'sks': 80,
#     'beasiswa': False,
#     'lahir': datetime.datetime(2002, 12, 19)
# }

# mhs2 = {
#     'nama': 'muhamamd rizki',
#     'nim': '5520120027',
#     'sks': 70,
#     'beasiswa': False,
#     'lahir': datetime.datetime(2001, 10, 10)
# }

# mhs3 = {
#     'nama': 'ummul hairiah',
#     'nim': '5520120028',
#     'sks': 75,
#     'beasiswa': True,
#     'lahir': datetime.datetime(2002, 9, 18)
# }

# data_mhs = {
#     'key1': mhs1,
#     'key2': mhs2,
#     'key3': mhs3,
# }

# print(f"{'KEY':<6} {'Nama':<17} {'SKS':<4} {'Beasiswa':<9} {'Lahir':<10}")
# print('-'*50)

# for mhs in data_mhs:
#     KEY = mhs
#     Nama = data_mhs[KEY]['nama']
#     sks = data_mhs[KEY]['sks']
#     beasiswa = data_mhs[KEY]['beasiswa']
#     lahir = data_mhs[KEY]['lahir'].strftime('%x')

#     print(f"{KEY:<6} {Nama:<17} {sks:<4} {beasiswa:<9} {lahir:<10}")

mhs_temp = {
    'nama': 'nama',
    'nim': '0000000000',
    'sks': 0,
    'lahir': datetime.datetime(1111,1,11)
}

data_mhs = {}   

index = 0
while True:
    os.system('cls')    # untuk clear terminal
    mhs = dict.fromkeys(mhs_temp.keys())

    mhs['nama'] = input('nama mahasiswa : ')
    mhs['nim'] = input('nim mahasiswa : ')
    mhs['sks'] = int(input('sks mahasiswa : '))
    thn = int(input('tahun lahir (YYYY) : '))
    bln = int(input('bulan lahir (1-12) : '))
    tgl = int(input('tanggal lahir (1-31) : '))
    mhs['lahir'] = datetime.datetime(thn, bln, tgl)

    # KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    index += 1
    KEY = index
    data_mhs.update({KEY: mhs})

    print(f"{'KEY':<6} {'Nama':<17} {'SKS':<4} {'Lahir':<10}")
    print('-'*50)
    for mhs in data_mhs:
        KEY = mhs
        Nama = data_mhs[KEY]['nama']
        sks = data_mhs[KEY]['sks']
        lahir = data_mhs[KEY]['lahir'].strftime('%x')

        print(f"{KEY:<6} {Nama:<17} {sks:<4} {lahir:<10}")
    
    print('\n')
    is_done = input('masih lanjut? (y/n)')
    if is_done == 'n' : break

