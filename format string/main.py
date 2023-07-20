#format string

#contoh format tring
nama = "Andi"
format_str = f"{nama}"
print(format_str)

#contoh format angka
angka = 2023.5
format_str_angka = f"{angka}"
print(angka)

#format boolean
boolean = True
format_boolean = f"{True}"
print(format_boolean)

#format bilangan bulat
integer = 10
format_int = f"{integer:d}"
print(format_int)

#format bilangan ribuan
ribuan = 2000
format_ribuan = f"bilangan ribuan = {ribuan:,}"
print(format_ribuan)

#format bilangan jutaan
jutaan = 2000000
format_jutaan = f"bilangan jutaan = {jutaan:,}"
print(format_jutaan)

#menampilkan bilangan desimal angka dibelakang koma (,)
angka1 = 2023.50009
format_str_angka1 = f"dua angka di belakang koma = {angka1: .2f}"
print(format_str_angka1)

#menampilkan leading zero
angka3 = 2023.5
format_str_angka2 = f"desimal = {angka3 : 010.2f}"
print(format_str_angka2)


#menampilkan tanda plus ( + ) atau minus ( - )
angak_minus = -10
angka_plus = +10
format_minus = f"format minus = {angak_minus:+d}"
format_plus = f"format plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

#menampilkan format pesentase
persentase = 0.035
format_persen = f"format persen = {persentase:.2%}"
print(format_persen)


#melakukan operasi aritmatika di dalam placeholder
price = 5000
qty = 10
aritmatika = f"jumlah = Rp {price*qty:,}"
print(aritmatika)

#format angka lain (binary, octal, hexadecimal)

nilai = 225
format_binary = f"binary {bin(nilai)}"
format_octal = f"octal {oct(nilai)}"
format_hexadecimal = f"hexadecimal {hex(nilai)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)