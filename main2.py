# operasi komparasi
# x = 5
# y = 5
# print('nilai x =', x, 'id =', hex(id(x)))
# print('nilai y =', y, 'id =', hex(id(y)))
# hasil = x is y
# print(hasil)

# operasi logika atau boolean

# NOT (kebalikan)
print('===== NOT =====')
a = True
c = not a
print('data a =', a)
print('data c =', c)

# OR (jika salah satu bernilai true, hasilnya true)
print('===== OR =====')
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)


# AND (jika salah satu bernilai false, hasilnya false / harus true semua)
print('===== AND =====')
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)

a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)

a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)

a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

# XOR (akan true, jika salah satu true dan sisanya false)
print('===== XOR =====')
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)