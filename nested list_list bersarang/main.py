#nested list / list bersarang

#list biasa
data_0 = [ 1, 2 ]
data_1 = [ 3, 4 ]

print(data_0)
print(data_1)

data_list_biasa = [ 1, 2, 3, 4 ]
print(f"list biasa {data_list_biasa}")

#maka untuk membuat list bersarang '/ nested list
list_2d = [data_0, data_1, data_list_biasa]
print(f"nested list menjadi : {list_2d}")


#nesx -> contoh penggunaan looping nested list
peserta_0 = ["andi", 30, "laki_laki"]
peserta_1 = ["winda", 25, "perempuan"]
peserta_2 = ["darma", 27, "laki_laki"]

list_peserta = [peserta_0, peserta_1, peserta_2]
#looping list peserta
for perserta in list_peserta:
    print(f"nama peserta \t: {peserta_0[0]}")
    print(f"nama peserta \t:{peserta_1[1]}")
    print(f"nama peserta \t:{peserta_0[2]}\n")
