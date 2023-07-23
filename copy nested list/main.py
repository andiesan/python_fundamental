#menduplikasi nested list

data_0 = [ 1, 2 ]
data_1 = [ 3, 4 ]
data_2d = [data_0, data_1]
print(f"print data {data_2d}")
data_2d_copy = data_2d.copy()
print(f"print data {data_2d}")
print(f"data_2d_copy {data_2d_copy}")

#mengambil nested list dengan index
data = data_2d[1][0] #mengambil data index kedua dan isi index pertama
print(f"data yang diambil adalah {data}")

#cek adress memory keduanya
print(f"data_2d asli adalah {hex(id(data_2d))}")
print(f"data_2d_copy hasil copy adalah {hex(id(data_2d_copy))}")
#maka data_2d asli dan data_2d_copy memiliki adres memory yang berbeda

#cek adress memory pada index kedua duanya
print(f"adress dari member ke- 1")
print(f"adress memory asli {hex(id(data_2d[0]))}")
print(f"adress memory copy {hex(id(data_2d_copy[0]))}")
#maka hasil adress memory masih sama
#maka untuk menduplikasi ( copy ) hanya bisa pada induk list
#dan tidak merubah adseess memory pada isi list / indexnya

#agar hasil copy dapat merubah isi index pada nested list
#perlu menggunakan method deepcopy
print("===deepcopy index isi list===")
#cara menggunakan deepcopy -> import module deepcopy
from copy import deepcopy
data_2d = [data_0, data_1]
data_2d_deepcopy = deepcopy(data_2d)
print(f"adress memory asli {hex(id(data_2d[0]))}")
print(f"adress memory deepcopy {hex(id(data_2d_deepcopy[0]))}")

