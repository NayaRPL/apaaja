print("lanjutan while")
baris=3
i=1
while i <= baris:
    print("makan")
    i+=1

print("menampilkan bilangan prima dari 1 sampai 100")
bilangan = int(input("masukkan angka yang di cek:"))
bilangan = int(bilangan)
pembagi=2
while bilangan % pembagi !=0:
    pembagi =pembagi + 1

if pembagi == bilangan:
    print("bilangan", bilangan, "adalah bilangan prima")
else:
    print("bilangan",bilangan,"adalah bukan bilangan prima")




