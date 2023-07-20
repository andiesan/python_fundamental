#date and time


#contoh date time data input
import datetime as dt
print("silakan masukan tanggal, \n bulan dan tahun" )
tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t: "))
tahun = int(input("tahun \t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")


#cari jumlah usia
hari_ini = dt.date(tahun,bulan,tanggal)
print(f"hari ini tanggal : { hari_ini }")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print ( umur_hari )

print(f"Harinya adalah : {tanggal_lahir:%A}")
print ( f"umur anda adalah : {umur_tahun} tahun")