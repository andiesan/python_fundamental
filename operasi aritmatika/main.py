#operasi aritmatika
# operasi standard

a = 5
b = 3
#pertambahan +
hasil = a + b
print(a,'+',b, "=", hasil)

#pengurangan -
hasil = a - b 
print(a,'-',b, "=", hasil)

#perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

#pembagian /
hasil = a / b
print( a,'/',b,'=',hasil)

#perpangkatan ** ( eksponen )
hasil = a ** b
print(a,'**',b,'=',hasil)

#modulus % ( sisa bagi)
hasil = a % b
print(a,'%',b,'=',hasil)

#Floor division // ( pembagian dengan pembulatan hasil )
hasil = a // b
print(a,'//',b,'=',hasil)

#operasional priority
#example :
x = 10
y = 3
z = 2
hasil = x + y - z ** x * y / z // x % y 
print(x, '+', y, '-', z, '**', x, '*', y, '/', z, '//', x, '%', y, '=', hasil )