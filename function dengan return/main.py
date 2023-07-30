'''function dengan return'''

#templete function dengan kembalian
    # def nama_function(argument)
        #badan function
        #return output
#function kuadrat dengan return
def quadrat(input_angka):
    '''function return quadrat'''
    output_quadrat = input_angka**2
    return output_quadrat

y = quadrat(5) # -> 5*5 / 5**2
print(y)

print(quadrat(6)) # -> 6*6 / 6**2

z = 10 + quadrat(2) # -> 10 + ( 2*2 / 2**2 )
print(z)


#function tambah dengan return
def function_tambah(angka1, angka2):
    '''function return tambah dengan multi input'''
    return angka1 + angka2

a = function_tambah(10,2)
print(a)


#function dengan banyak return
def operasi_aritmatik(angka3, angka4):
    tambah  = angka3 + angka4
    kurang  = angka3 - angka4
    kali    = angka3 * angka4
    bagi    = angka3 / angka4
    modulus = angka3 % angka4
    kuadrat = angka3 ** angka4
    return tambah, kurang, kali, bagi, modulus, kuadrat

o, p, q, r, s, t = operasi_aritmatik(3,2)
print(f"hasil tambah = {o}")
print(f"hasil kurang = {p}")
print(f"hasil kali = {q}")
print(f"hasil bagi = {r}")
print(f"hasil modulus = {s}")
print(f"hasil kuadrat = {t}")
