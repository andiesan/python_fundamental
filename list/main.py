#list / array di bahasa pemograman lain
#example list

# list integer
number = [0,1,2,3,4,5] #kumpulan data interger
print(number)

string = ["sendal, sepatu, payung, meja"] #kumpulan data string
print(string)

boolean = ["True, False, False, True"] #kumpulan data boolean
print(boolean)

campur = [1, "meja", True, 3, False, "kursi"] #kumpulan data campuran
print(campur)

#cara alternatif membuat list
data_range = range(0,10,2) #-> start, stop, step.
print(data_range)
data_list = list(data_range) #list -> method untuk membuat list
print(data_list)

#cara membuat list dengan for loop ( list chompension )
list_pake_for = [ i for i in range( 0, 10 )]
print(list_pake_for)

#membuat list dengan for dan if
list_pake_for_if = [ i for i in range( 0, 8 ) if i != 3]
#maka angka 3 tidak ditampilkan oleh loop
print(list_pake_for_if)