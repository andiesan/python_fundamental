#copy dan pop dictionary
teman_teman = {
    "cup"   : "surucup",
    "dan"   : "suradan",
    "mia"   : "sarmia",
    "tong"  : "surotong",
    "mila"  : "karmila"
}

friends = teman_teman
print(f"ini adalah teman teman : {teman_teman}\n")
print(f"ini adalah data friends : {friends}\n")

#menggunakan properties copy ()
friends_copy = teman_teman.copy()
teman_teman["cup"] = "ucup surucup"
print("print hasil copy") 
print(f"ini adalah teman teman : {teman_teman}\n")
print(f"ini adalah data friends : {friends_copy}\n")

#pop dictionary ( mengambil data berdasarkan keys)
dataDan = friends.pop("dan")
print(f"data data dan : {dataDan}\n")
#maka hasil data dan telah di ambil dan dipisahkan dari dictionary
print(f"data friends : {friends}\n")

#popitem dictionary ( mengambil data terakhir pada dictionary )
dataTerakhir = friends.popitem()
print(f"data terakhir : {dataTerakhir}\n")
#maka hasil data terakhir telah dipisahkan dari dictionary
print(f"data friends : {friends}\n")