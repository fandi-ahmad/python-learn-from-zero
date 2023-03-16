def hello(params):
    print(f'hello {params}')

def tambah(angka):
    hasil = angka+10
    return hasil

a = tambah(8)

def operasi(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah, kurang, kali, bagi

# print(operasi(10, 5))
k,l,m,n = operasi(10, 5)

def say_hello(params = 'kamu'):     # 'kamu' adalah default jika paramsnya kosong
    print(f'hello {params}')

say_hello('fandi')
say_hello()

def nambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output

hasil = nambah(20,30,4)
print(f'hasil = {hasil}')

def tes_kwargs(**kwargs):
    print(kwargs)
    print(kwargs['nama'])

tes_kwargs(nama='fandi', tinggi=270, berat=50)

def math(*args, **kwargs):
    output = 0
    if kwargs['option'] == 'tambah':
        print('penjumlahan')
        for a in args:
            output += a
    elif kwargs['option'] == 'kali':
        print('perkalian')
        output += 1
        for a in args:
            output *= a
    else:
        print('tidak ada operasi')

    return output

hasil_lain = math(1,2,3,4,5, option='kali')
print(hasil_lain)

global_angka = 0
global_nama = 'fandi'

def ubah_angka(nilai_baru, nama_baru):
    global global_angka         # untuk mendapat akses ke variabel global (hanya berlaku untuk penggunaan fungsi)
    global global_nama
    global_angka = nilai_baru
    global_nama = nama_baru

print(global_angka, global_nama)
ubah_angka(20, 'ahmad')
print(global_angka, global_nama)


# contoh lain
angka_lain = 0

for i in range(0,5):
    angka_lain += 1
    angka_dummy = 8

print(angka_lain)
print(angka_dummy)

if True:
    angka_lain = 12
    angka_dummy = 9

print(angka_lain)
print(angka_dummy)

# for dan if, masih bisa menggunakan variabel global scope
