'''default argument function'''

#templete default argument function :
#def function ( argument = nilai defaultnya )
#example 1
def say_hello( nama = "andi sanjaya" ):
    '''function dengan default argument'''
    print(f"hallo {nama}")
say_hello() # -> panggil function


#example 2
'''function default dengan 2 argument'''
def katakan( kepada, pesan = "apa kabar"):
    '''function dengan 1 input biasa dan 1 default'''
    print(f"katakan {pesan}, {kepada}")

katakan("hai ganteng, andi")

#example 3
'''defaul argument function dengan return'''
def hitung_pangkat(angka, pangkat = 2):
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat(2,4))
#call function 
hasil = hitung_pangkat(angka = 5, pangkat = 2)
print(hasil)


#example 4
'''dafault argument function dengan banyak argument'''
def function ( input1 = 1, input2 = 2, input3 = 3, input4 = 4, input5 = 5 ):
    hasil = input1 + input2 + input3 + input4 + input5
    return hasil

#call function
print(function())
# call function dengan merubah input dengan cara mengirimkan parameter
# merubah argument input 3 dengan nilai angka 10
print(function(input3 = 10))
