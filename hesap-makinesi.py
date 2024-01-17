while True :

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

    # Kullanıcının seçim yapması
    secim = input("--> Yapmak istediğiniz işlemin numarasını yazınız : ")
    if secim != "1" and secim != "2" and secim != "3" and secim != "4" :
        print("Yanlış seçim yaptınız, lütfen kontrol ediniz.!!!")
    else :
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
                veri = int(veri)
                veriler.append(veri)
            i = i + 1
        print("-----------------------")
        print(f"Girişini yaptığınız veriler : {veriler}")
        print("-----------------------")
        # işlemler
        if secim == "1" :
            index_no = 0
            sonuc = 0 # sonuc = veriler[1]
            while index_no < len(veriler) :
                sonuc = sonuc + veriler[index_no]
                index_no += 1 # index_no = index_no + 1
                # print(sonuc)
            #islem_sonucu = sayı1 + sayı2
            #print(f"Toplama işleminin sonucu = {islem_sonucu}")
        elif secim == "2" :
            index_no = 1
            sonuc = veriler[0]
            while index_no < len(veriler) :
                sonuc = sonuc - veriler[index_no]
                index_no += 1 # index_no = index_no + 1
            #islem_sonucu = sayı1 - sayı2
            #print(f"Çıkarma işleminin sonucu = {islem_sonucu}")
        elif secim == "3" :
            index_no = 0
            sonuc = 1 # sonuc = veriler[1]
            while index_no < len(veriler) :
                sonuc = sonuc * veriler[index_no]
                index_no += 1 # index_no = index_no + 1
        elif secim == "4" :
            index_no = 1
            sonuc = veriler[0]
            while index_no < len(veriler) :
                sonuc = sonuc / veriler[index_no]
                index_no += 1 # index_no = index_no + 1
        else :
            print("Yanlış seçim yaptınız, lütfen kontrol ediniz.!!!")
        # Çıktılar
        print(f"İşleminizin sonucu = {sonuc}")
        # print("Program kapatılıyor")
    
    print()
    print("============================================")
    secim = input("Devam etmek istiyor musunuz ? (E/H) : ")
    if secim == "H" or secim == "h":
        print("Program kapatılıyor")
        print()
        break
