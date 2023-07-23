#dictionary

#list adalah array yang dapat diakses menggunakan index
#contoh
data_list = ["andi", "rizal", "david"]
print(data_list)
#mengambil index
print(data_list[0])


#dictionary (dict) -> adalah array accociative ( assoc array )
#menggunakan identifier -> key
#identifier sebagai inisialisasi
#key sebagai value
#untuk membuat dictionary menggunakan kurung kurawal {}

#contoh 
data_dict = {
    'init1'    : 'value1',
    'init2'    : 'value2',
    'init3'    : 'value3',
    'init4'    : 'value4',
    'number'   : 1200,
    'data_list': data_list
}

print(data_dict)
#untuk mengambil data pada dictionary tidak menggunakan index
#mengambil data pada dictionary menggunakan key
#contoh :
print(data_dict['init1'])
#maka value yang ditampilkan adalah value1
print(data_dict['number'])
print(data_dict['data_list'])