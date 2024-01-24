# menü
def menu():
    # Yapılacak işlemlerin çıktısı
    print("HESAP MAKİNESİ PROGRAMI")
    print("-----------------------")
    menü = """
    Yapılabilir işlemler :
        1- Toplama
        2- Çıkarma
        3- Çarpma
        4- Bölme
        5- Üs alma
        6- Çıkış için ( Ç/ç ) harfine basınız.
    """
    print(menü)
    print("-----------------------")

# kullanıcı seçimi
def islem_secme() -> str:
    secim = input("Yapmak istediğiniz işlemin numarasını giriniz :")
    return secim

# veri girişi
def veri_girisi() -> list:
    # Kullanıcıdan verilerin alınması
    print("-----------------------")
    print("Veri Girişi")
    veriler = []
    i = 1
    
    while True:
        veri = input(f"{i}. sayıyı giriniz ( Veri girişini tamamlamak için 'ç' harfine basınız!): ")
        if veri == "ç" or veri == "Ç" :
            break
        else :
            try:
                veri = int(veri)
            except:
                print("=======================================================")
                print("YANLIŞ VERİ GİRDİNİZ, GİRDİĞİNİZ VERİLERİ KONTROL EDİNİZ")
                print("=======================================================")
                # ana_fonksiyon()
            else:
                veriler.append(veri)
                i = i + 1
    print("-----------------------")

    return veriler
    # girilen veriler kontrol edilmiyor
    # hata denetimi

# toplama
def toplama(veriler:list):
    sonuc = 0
    for sayi in veriler :
        sonuc = sonuc + sayi
    print(f"Toplama işleminin sonucu : {sonuc}")

# çıkarma
def cikarma(veriler:list):
    sonuc = veriler[0]
    for index_no in range(1, len(veriler)) :
        sonuc = sonuc - veriler[index_no]
    print(f"Çıkarma işleminin sonucu : {sonuc}")

# çarpma
def carpma(veriler:list):
    sonuc = 1 # sonuc = veriler[1]
    for sayi in veriler :
        sonuc = sonuc * sayi
    print(f"Çarpma işleminin sonucu : {sonuc}")

# bölme
def bolme(veriler:list):
    sonuc = veriler[0]
    for index_no in range(1,len(veriler)):
        sonuc = sonuc // veriler[index_no]
    print(f"Bölme işleminin sonucu : {sonuc}")

def us_alma(veriler):
    pass

# çıkış
def cikis():
    print("==============================")
    print("Programdan çıkış yapılıryor...")
    exit()

# ana fonksiyon
def ana_fonksiyon():
    while True :
        menu()
        secim = islem_secme()
        print(f"Seçmiş olduğunuz işlem numarası : {secim}")
        if secim == "6" or secim == "Ç" or secim == "ç":
            cikis()
        else:
            veriler =  veri_girisi()
        print()
        print(f"Girmiş olduğunuz veriler : {veriler}")

        match secim :
            case "1" :
                toplama(veriler)
            case "2" :
                cikarma(veriler)
            case "3" :
                carpma(veriler)
            case "4" :
                bolme(veriler)
            case "5" :
                us_alma(veriler)
            case "6" :
                cikis()
        print()
        print("=======================================")
        print()    

if __name__ == "__main__":       
    ana_fonksiyon()
