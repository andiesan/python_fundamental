#break
#example

angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    while angka == 3:
        print("nice !")
        break # -> ketika break ini digunakan pada looping ketika hanya akan
            # mengeprint ( "nice !") lalu looping akan berhenti
    print("whatsupp")
print("stop")