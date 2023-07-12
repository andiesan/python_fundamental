#operasi comparasi ( perbandingan )
#setiap hasil dari operator komparasi adalah boolean
# > , < , >= , <= , ==, !=, is, is not

#is dan is not sebagai comparasi object identity
#example :
x = 5
y = 5
print('nilai x =', x ,'id =',hex(id(x)))
print('nilai y =', y ,'id =',hex(id(y)))
hasil = x is y
print('hasil = ', hasil)

a = 3
b = 2
hasil = a is not b
print('hasil = ', hasil)