#string width dan aligment

data_nama = "Andi Sanjaya"
data_umur = 31
data_berat = 50
data_tinggi = 170
#string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, berat = {data_berat}, tinggi = {data_tinggi}"
print(5*"="+"data_string"+"="*5)
print(data_string)

#string multiline dengan menggunakan ( newline, enter \n )
data_string1 = f"nama = {data_nama}, \n umur = {data_umur}, \n berat = {data_berat}, \n tinggi = {data_tinggi}"
print(5*"="+"data_string1"+"="*5)
print(data_string1)

#string multiline dengan menggunakan ( triple kutip """)
data_string2 = f"""
nama = {data_nama}
umur = {data_umur}
berat = {data_berat} 
tinggi = {data_tinggi}
"""
print(5*"="+"data_string2"+"="*5)
print(data_string2)

#setting width menggunakan tab pada string dan arraaw pada variable
data_string2 = f"""
nama    = {data_nama:>10}
umur    = {data_umur:>10}
berat   = {data_berat:>10} 
tinggi  = {data_tinggi:>10}
"""
print(5*"="+"data_string2"+"="*5)
print(data_string2)
