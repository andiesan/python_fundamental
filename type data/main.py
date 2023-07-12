#type data

# type data angka satuan ( interger )
interger = 1
# inisialisai type data 
print(interger, "adalah")
print (type(interger))# maka 1 adalah interger

#type data pecahan ( float )
float = 5.5
print(float)
print(type(float))# maka 5 adalah float

#type data caracter ( string )
string = "nama"
print(string)
print(type(string))# maka "nama" adalah string

#type data benar/salah atau 1/0 ( boolean )
benar = True
print(benar)
print(type(benar))# maka true adalah boolean

#type data khusus ( kompleks ) dapat digunakan secara langsung
#untuk operator bilangan 
kompleks = complex(5,6)# untuk type data ini, inisialisasi data diawali dengan complex
print(kompleks)
print(type(kompleks))

#type data dari bahasa C
#untuk menggunakan type data bahasa C perlu melakukan import library
#exampe : dari bahasa C
from ctypes import c_double
data_c_double = c_double(20.50)
print(data_c_double)
print(type(data_c_double))




