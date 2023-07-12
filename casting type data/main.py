#casting type data adalah merubah dari satu type data ke type data lain
data_int = 9;
print("data", data_int,", type",type(data_int))
#type data phyton = int,float,string,boolean

#contoh casting data_int diatas
print("===contoh int===")
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data", data_float,", type",type(data_float))
print("data", data_str,", type",type(data_str))
print("data", data_bool,", type",type(data_bool))
#nilai boolean akan menjadi false jika nilai type data adalah 0


print("===contoh float===")
data_float = 9.5;
print("data", data_float,", type",type(data_float))

data_float = int(data_float) # nilai akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data", data_float,", type",type(data_float))
print("data", data_str,", type",type(data_str))
print("data", data_bool,", type",type(data_bool))
#nilai boolean akan menjadi false jika nilai type data adalah 0


print("===contoh boolean===")
data_bool = False;
print("data", data_bool,", type",type(data_bool))

data_float = int(data_float) # nilai akan dibulatkan kebawah
data_str = str(data_float)
data_bool = float(data_float)
print("data", data_float,", type",type(data_float))
print("data", data_str,", type",type(data_str))
print("data", data_bool,", type",type(data_bool))
#nilai boolean akan menjadi false jika nilai type data adalah 0