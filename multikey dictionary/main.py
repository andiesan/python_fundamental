#multikey dictionary

#multikey dictionary -> manjadikan beberapa dictionary untuk ditampilkan sebagai value -
# - pada dictionary lain
import datetime # untuk menghitung waktu secara otomatis
#example 
mahasiswa_0 = {
    "nama"      : "Asep",
    "alamat"    : "bogor",
    "nilai"     : 80,
    "beasiswa"  : False,
    "lahir"     : datetime.datetime(2000, 2, 29) # format tahun/bulan/tanggal
}

mahasiswa_1 = {
    "nama"      : "Rudy",
    "alamat"    : "bandung",
    "nilai"     : 76,
    "beasiswa"  : False,
    "lahir"     : datetime.datetime(2003, 3, 29) # format tahun/bulan/tanggal
}

mahasiswa_2 = {
    "nama"      : "Andi",
    "alamat"    : "jakarta",
    "nilai"     : 90,
    "beasiswa"  : True,
    "lahir"     : datetime.datetime(2001, 10, 25) # format tahun/bulan/tanggal
}

mahasiswa_3 = {
    "nama"      : "Mirna",
    "alamat"    : "bogor",
    "nilai"     : 85,
    "beasiswa"  : True,
    "lahir"     : datetime.datetime(2002, 12, 9) # format tahun/bulan/tanggal
}

mahasiswa_4 = {
    "nama"      : "Kayla",
    "alamat"    : "Surabaya",
    "nilai"     : 79,
    "beasiswa"  : False,
    "lahir"     : datetime.datetime(2004, 4, 30) # format tahun/bulan/tanggal
}

data_mahasiswa = {
    "MAH00" : mahasiswa_0,
    "MAH01" : mahasiswa_1,
    "MAH02" : mahasiswa_2,
    "MAH03" : mahasiswa_3,
    
}

print(f"{'KEY'}\t\t{'nama'}\t\t{'alamat'}\t\t{'nilai'}\t\t{'beasiswa'}\t\t{'lahir'}") 
print("_"*100)

#proses looping untuk menampilkan value data_mahasiswa
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    ALAMAT = data_mahasiswa[KEY]['alamat']
    NILAI = data_mahasiswa[KEY]['nilai']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY}\t\t{NAMA}\t\t{ALAMAT}\t\t{NILAI}\t\t{BEASISWA}\t\t\t{LAHIR}") 