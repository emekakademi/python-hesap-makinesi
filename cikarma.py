veriler = [100, 20, 10 ,20,70]
index_no = 1
sonuc = veriler[0]
while index_no < len(veriler) :
    sonuc = sonuc - veriler[index_no]
    index_no += 1 # index_no = index_no + 1
    print(sonuc)

print(sonuc)
