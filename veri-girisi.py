# global değişkenler - heryerden erişebiliriz.
veriler = []
i = 1
while True:
    veri = input(f"{i}. sayıyı giriniz ( Veri girişini tamamlamak için 'ç' harfine basınız!): ")
    if veri == "ç" or veri == "Ç" :
        break
    else :
        veri = int(veri)
        veriler.append(veri)
    i = i + 1

print(veriler)