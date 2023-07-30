'''keyword args (kwargs) pada function '''

#example function biasa
def function(nama, tinggi, berat):
    '''function biasa'''
    print(f"{nama}, punya tinggi = {tinggi}, dan berat = {berat}")

function("ucup", 170,50)

#example function dengan kwargs
def function_kwargs(**kwargs):
    '''function kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama}, punya tinggi = {tinggi}, dan berat = {berat}")

function_kwargs(nama="ucup", tinggi=170, berat=50 )
    
'''study kasus'''
def math(*args, **kwargs):
    output = 0
    if kwargs ["option"] == "tambah":
        print("operasi penjumlahan")
        for angka in args:
            output += angka
    elif kwargs ["option"] == "kali":
        print("operasi perkalian")
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")
    
    return output

hasil = math(1,2,3,4,5,6, option="tambah")
print(f"hasil jumlah = {hasil}")
hasil = math(1,2,3,4,5,6, option = "kali")
print(f"hasil kali = {hasil}")
