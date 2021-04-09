#program menghitung rata rata bilangan
Prog = "PROGRAM MENGHITUNG RATA-RATA"
print(Prog.center(50))

#input bilangan
Bilangan = []
Jumlah = 0

#input banyak bilangan
n = int(input("Banyak bilangan: "))

#program menghitung rata rata
for number in range(0, n):
    Komponen = int(input("Masukkan bilangan ke-%d =" % (number+1)))
    Bilangan.append(Komponen)
    Jumlah = Jumlah + Bilangan[number]
    Mean = Jumlah / n
print("\nRata-rata", n, "bilangan tersebut yaitu %0.2f" % Mean)

