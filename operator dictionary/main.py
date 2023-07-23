#operator dictionary

data_dict = {
    'cup'   :'surucup',
    'ton'   :'surotong',
    'dan'   :'dadang',
}

#panjang dictionary menggunakan LANDICT 
print("\n ===LANDICT===")
LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}")

#mengecek key ada atau tidak dengan KEY dan CHEKKEY
print("\n ===KEY dan CHECKKEY===")
KEY = 'cup'
CHEKKEY = KEY in data_dict
print(f"apakah {KEY}, ada di dalam data_dict {CHEKKEY}")

#mengakses data ( value ) dengan GET
print("\n === get ===")
print(data_dict['cup'])

print(data_dict.get('cup')) #data tersedia
print(data_dict.get('kis')) #contoh data tidak tersedia
#secara default hasil yang di tampilkan adlah ( none )
print(data_dict.get('kis','data tidak ditemukan'))
#contoh data yang tidak tersedia ditampilkan dengan pesan ( mesege )
#data tidak tersedia ditampilkan dengan menambahkan parameter ke - 2
#parameter ke 2 - yaitu : 'data tidak ditemukan'

#mengupdate data dengan update()
print("\n ===update===")
#cara pertama tanpa update
data_dict['cup'] = 'ucup si ganteng'
print(data_dict)
print('')
#cara kedua menggunakan update()
data_dict.update({'cup': 'ucup surucup'})
print(data_dict)


#menambah data juga dapat dilakukan dengan update()
#jika data yang di update tidak tersedia -
#maka program secara otomatis akan menambhakan data baru
#menambahkan data baru
print("\n ===tambah data===")
data_dict.update({'dis' : 'andisan'})
print(f"data baru berhasil di tambahkan : \n {data_dict}")

#menghapus data dengan menggunakan del
print("\n ===del (delete)===")
del data_dict['dis']
print(data_dict)
#maka 'dis' : 'andisan' telah dihapus
