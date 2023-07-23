#looping dictionary

teman_teman = {
    'cup'   : 'ucup surucup',
    'ton'   : 'otong surotong',
    'dan'   : 'dadan suradan',
    'dis'   : 'dis anandis'
}

#looping menggunakan for
#maka yang dihasilkan adalah keynya
for teman in teman_teman:
    print(teman)

#operator untuk mengambil item / iteration ( iterable )
#cara pertama mengambil keys
print("\n ===cara mengambil keys===")
key = teman_teman.keys()
print(key)

for key in teman_teman.keys():
    print(teman_teman.get(key))

#cara kedua  mengambil values
print("\n ===cara mengambil values===")
values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

#cara ketiga mengambil tuples
print("\n ===cara mengambil item (tuples)===")
for item in teman_teman.items():
    print(item)

#cara keempat mengambil data complex
print("\n ===mengambil data complex===")
for key,value in teman_teman.items():
    print(f"key = {key},\t value = {value}")