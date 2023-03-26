# __main__

# __name__ == ""__main__"   akan terjadi jida ada di file progam utama
# print(__name__)


# def tambah(a,b):
#     return a+b

# if __name__ == '__main__':
#     angka1 = 5
#     angka2 = 10
#     hasil = tambah(angka1, angka2)
#     print(hasil)


# ===== READ EXTERNAL FILE =====
file = open('data.txt', mode='r')

# print(file.read())

print(file.readline(), end='')
print(file.readline(), end='')


# close / menutup file yang dibuka
file.close()

# pakai cara ini supaya file yang dibuka tidak perlu di close
with open('data.txt', mode='r') as file:
    content = file.readline()
    print(content, end='')


# ===== WRITE EXTERNAL FILE =====
# *ketika file data.txt tidak ada, maka akan membuat file baru dengan nama data.txt
# with open ('data.txt', 'w', encoding='utf-8') as file:
#     file.write('text pertama\n')

# with open ('data.txt', 'a', encoding='utf-8') as file:
#     file.write('text yang baru dari main10.py, tapi pake a\n')

# with open ('data.txt', 'a', encoding='utf-8') as file:
#     file.write('text baru yang ditimpa\n')

# with open ('data.txt', 'a', encoding='utf-8') as file:
#     file.write('apa lagi ya?\n')


with open ('data.txt', 'r+', encoding='utf-8') as file:
    file.write('baris 1 \n')
    file.write('baris 2 \n')
    data = file.read()
    print(data)

with open ('data.txt', 'r+', encoding='utf-8') as file:
    file.write('baris 3 \n')

