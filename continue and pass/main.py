#continus and pass

#pass -> adalah dummy yang tidak akan di eksekusi
#example 
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass # -> ini tidak akan di eksekusi
    print(angka)

#continus
number = 0
print(f"number sekarang {number}")
while number < 10:
    number += 1
    print(f"number sekarang {number}")
    if number == 3:
        print("nice")
        continue # -> hanya akan menampilkan nice lalu dilanjutkan ke perulangan selanjutnya
    print("whatsupp")
    print("finish !")