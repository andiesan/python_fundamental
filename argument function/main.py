'''function dan argument input'''

#templete dan strucktur
    # def nama function
    # badan function

def hello_world(nama): # (nama) -> param
    '''function hello world menerima input dengan param variable'''
    print(f"selamat datang dunia {nama}")
    
hello_world("andi") # (andi) -> adalah parameter input yang dikirimkan

'''example function dengan aritmatik'''
def math(angka1, angka2):
    '''function math tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
math(1,4)

'''contoh argument funtion untuk list'''
'''looping list di dalam function'''
def say_hi(list_peserta):
    '''function say_hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
     print(f"daftar anggota {peserta}")
# mendefinisikan input untuk parameter yang dikirimkan
anggota_peserta = ["andi", "ridwan", "anggi"]
say_hi(anggota_peserta)