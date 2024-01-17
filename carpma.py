veriler = [1,2,3,4]
index_no = 0
sonuc = 1 # sonuc = veriler[1]
while index_no < len(veriler) :
    sonuc = sonuc * veriler[index_no]
    index_no += 1 # index_no = index_no + 1

print(sonuc)
