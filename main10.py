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



