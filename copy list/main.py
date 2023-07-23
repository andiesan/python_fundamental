#copy list ( teknik duplikasi list )

a = ["ucup", "otong", "dudung"]

b = a
print(f"print list a {a}")
print(f"print list b {b}")
#untuk merubah menduplikasi member a
print("membuat list c dengan dengan method copy() dari list a")
c = a.copy()

#cek adress memory pada list
print(f"adress memory a {hex(id(a))}")
print(f"adress memory b {hex(id(b))}")
print(f"adress memory c {hex(id(c))}")

#skrip di atas teridentifikasi bahwa 
#c memiliki list yang sama, akan tetapi memiliki address memory yang berbeda

print("merubah index pada list")
c[0] = "dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")