#looping list dan enumerate

#looping list menggunakan for loop
seri_angka = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
for seri in seri_angka: #seri - > inisialisasi variable yang di buat untuk isi list
    print(f"angka = {seri}")

#for loop string
print("\n===for loop string===")
member = [ "andi", "ari", "najwa", "lukman", "heru"]
for nama in member:
    print(f"nama member : {nama}")

#looping menggunakan for loop dengan range ( panjang )
print("\n===for loop dengan range===")
himpunan_angka = [ 9, 8, 7, 6, 5, 4, 3 ]
panjang = len(himpunan_angka)
print(panjang)

for inisial in range(panjang):
    print(f"angka = {himpunan_angka[inisial]}")

#looping menggunakan while loop
print("\n===loop menggunakan while===")
himpunan_angka = [ 9, 8, 7, 6, 5, 4, 3 ]
panjang = len(himpunan_angka)
i = 0
while i < panjang:
    print(f"angka = {himpunan_angka[i]}")
    i += 1

#looping menggunakan list comphension
print("\n===list cohompension===")
data = [ "andi", 1, 2, 3, "sans" ]
#penulisan sbb:
[print(i) for i in data ]
#jika dengan format sbb:
print("")
[print(f"data = {i}") for i in data]

#looping menggunakan enumerate
print("\n****enumerate****")
data_list =  [ "andi", 1, 2, 3, "sans" ]

#cara penulisan ( struktur penulisan ) sbb:
for index, data in enumerate(data_list):
    print(f"index = {index} adalah \t data = {data}" )

#note 
print("maka memiliki kelebihan yaitu enumerate \nakan menghasilkan inisialisasi index pada isi list")