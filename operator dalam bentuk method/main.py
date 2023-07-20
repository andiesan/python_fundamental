#operator dalam bentuk method
##merubah karakter (case) string

#merubah ke Upper case
apakabar = 'bro !'
print(apakabar.upper())

#merubah ke lowe case 
lebay = 'GUE GANTENG GAK BRO ?'
print(lebay.lower())

#pengecekan dengan is method
#contoh pengecekan lower case dan uppercase menggunakan is
hello = 'apa kabar'
apakah_lower = hello.islower()
print(hello,'apakah lowercase :',apakah_lower)
hello = 'apa kabar'
apakah_lower = hello.isupper()
print(hello,'apakah uppercase :',apakah_lower)


#isalpha --> untuk mengecek apakah semuanya huruf
#isalnum --> untuk mengecek apakah huruf dan angka
#isdecimal --> untuk mengecek apakah angka saja
#isspace --> untuk mengecek apakah ada spaci/tab/newline
#istitle --> untuk mengetahui apakah diawali dengan huruf besar
#isdigit --> untuk mengecek jumlah karakter angka

#contoh istitle
judul = 'Transformers'
hasil = judul.istitle()
print(hasil) # hasil akan bernilai boolean

#ngecek komponent dengan startswith dan  endswith 
cek_start = 'Andi Sanjaya'.startswith('Andi')
print(str(cek_start))
cek_end = 'Andi Sanjayas'.endswith('Sanjayas')
print(str(cek_end))

#penggabungan komponen string dengan join() dan split()
#join ( menggabungkan )
pisah = ['i', 'love', 'you']
print(pisah)
gabungan1 = ','.join(pisah)# dengan koma
print(gabungan1)
gabungan2 = ' '.join(pisah)# dengan spasi
print(gabungan2)
#split ( pisahkan )
gabungan3 ="akuehmsayangehmkamuehm"
pisahkan = 'ehm'.split(gabungan3)
print(pisahkan)


#alokasi karakter dengan rjust() ljust() center()
# - rjust ( right justify )
# - ljust ( left justify )
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(10)
print("'"+tengah+"'")

