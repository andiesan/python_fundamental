#operasi dan manipulasi string

#menyambung string atau concat ( concatenetion )
#example 
nama_depan = "Andi"
nama_tengah = "Sanjaya"
nama_belakang = "Deboras"
nama_lengkap = (nama_depan+' '+nama_tengah+' '+nama_belakang)
print(nama_lengkap)
#menghitung panjang string dengan (len)
panjang = (len(nama_depan))
print('Jumlah karakter nama depan adalah :', str(panjang), 'karakter')

#looping string 
print ( 'wk'*10 )
print ( 10*'wk')

#indexing 
print('index ke 0 adalah '+' '+nama_lengkap[0])
print('index ke 7 adalah '+' '+nama_lengkap[7])