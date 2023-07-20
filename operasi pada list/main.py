#operasi pada list

#example 
#mengambil informasi jumlah data
data_int = [ 1, 2, 3, 5, 7, 4, 2, 7, 9, 6, 3, 2 ]
database = len(data_int)
print(f"info jumlah data pada list -> \n {database}")

#menurutkan data_int diatas
data_sort = data_int.sort()
print(f"data_int diurutkan menjadi -> \n {data_sort}")

#melakukan count / menghitung data
print(f"tampilkan data -> {data_int}")
jumlah_data_2 = data_int.count(2)
jumlah_data_7 = data_int.count(7)
print(f"jumlah data 2 = {jumlah_data_2}")
print(f"jumlah data 7 = {jumlah_data_7}")

#menampilkan posisi data index
data = [ "andi", "ridwan", "rizki", "mawar" ]
print(f"data = {data}")
index_andi = data.index("andi")
index_rizki = data.index("rizki")
print(f"index andi adalah index ke -> {index_andi}")
print(f"index rizki adalah index ke -> {index_rizki}")

#membalik urutan data pada list menggunakan property reverse
data_int.reverse()
data.reverse()
print(f"kebalikan urutan data_int = \n {data_int}")
print(f"kabalikan urutan data_reverse = \n {data}")