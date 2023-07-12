#operasi logika atau boolean
# and, not, or, xor

print('=====not=====')
a = False
b = True
c = not a
print('a =', a)
print('c =', c)

print('====or====')# jika salah satu true, maka hasilnya true
d = a or b
print(a, 'or' ,b, '=', d)

print('====and====')# jika kedua duanya adalah true, maka hasilnya true
e = a and b
print(a, 'or' ,b, '=', e)

print('====xor (^)====')# akan menjadi true jika salah satu true
f = a ^ b
print(a, 'or' ,b, '=', f)