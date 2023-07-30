'''args'''
# memasukan data/ argument sebagai parameter
def function(nama, tinggi, berat):
    print(f"{nama}, punya tinggi = {tinggi}, dan berat = {berat}")

function("ucup", 170,50)

def function2(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama}, punya tinggi = {tinggi}, dan berat = {berat}")
function2(["otong", 150, 100])

#function menggunakan args
def function3(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama}, punya tinggi = {tinggi}, dan berat = {berat}")

function3("dudung", 160, 70)

# args dengan operasi aritmatika dan looping 
def tambah(*data):
    '''data typenya adalah tuple yang bisa di iterasi (iteration)'''
    output = 0
    for angka in data: # mulai menjumlahkan dengan looping
        output += angka

    return output # mengembhalikan nilai
hasil = tambah(1,2,3,4,5,6) # call function tambah
print(f"hasil = {hasil}")

hasil2 = tambah(10,10,4)
print(f"hasil2 = {hasil2}")

'''note : function dengan args menjadi lebih dinamic'''
