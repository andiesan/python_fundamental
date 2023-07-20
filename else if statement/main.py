#elif ( else if ) statement

#jika if adalah kondisi awal
#maka elif ( else if ) adalah kondisi kedua dan seterusnya

#example
nama = input("sebutkan namamu ?")
if nama == "andi san":
    print(f"trimakasih {nama}")
elif nama == "Rudi":
    print(f"kamu bukan andi")
else:
    print("kamu bukan keduanya")