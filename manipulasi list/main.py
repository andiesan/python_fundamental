#manipulasi data list

#menambah item pada list sesuai posisi
#list index 0(-4) 1(-3)  2(-2)   3(-1)
data = [ "andi", "beni", "rudi", "sumi"]
print(f"data sebelum ditambah = \n {data}")

data.insert(2,"asep") #2 -> adalah index "asep" -> adalah object yang ditambahkan
print(f"data sesudah ditambah = \n {data}")

#menambah item di akhir list
data.append("jajang") #append secara otamatis menambahkan object di akhir list
print(f"menambah data diakhir = \n {data}")

#menambah list dengan list 
data_baru = ["ujang", "dadan", "deden", "nurman"]
data.extend(data_baru)
print(f"menambah data dengan list = \n {data}")

#merubah data
#merubah data pada index ke 2
data[2] = "micheal"
print(f"data pada index ke 2 dirubah menjadi -> \n {data}") #micheal

#menghapus data dengan properties remove
data.remove("andi")
print(f"data remove -> \n {data}")

#remove data paling akhir secara otomatis
data.pop() #property pop secara otomatis akan menghapus data akhir
print(f"data akhir akan terhapus -> \n {data}")