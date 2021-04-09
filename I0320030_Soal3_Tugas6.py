#membuat program penentuan bilangan prima dan bukan bilangan prima
awal = 10 #awal
akhir = 24 #akhir

for a in range(awal, akhir + 1):
    if a > 1:
        for b in range(2, a):
            if (a % b) == 0 :
                #bilangan tersebut bukan bilangan prima
                print(a, "bukan prima")
                break
        else:
            #bilangan tersebut bilangan prima
            print( a, "adalah bilangan prima")