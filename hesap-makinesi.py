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
        sayı1 = int(input("Birinci sayıyı giriniz : "))
        sayı2 = int(input("İkinci sayıyı giriniz : "))
        print("-----------------------")
        # işlemler
        if secim == "1" :
            islem_sonucu = sayı1 + sayı2
            #print(f"Toplama işleminin sonucu = {islem_sonucu}")
        elif secim == "2" :
            islem_sonucu = sayı1 - sayı2
            #print(f"Çıkarma işleminin sonucu = {islem_sonucu}")
        elif secim == "3" :
            islem_sonucu = sayı1 * sayı2
            #print(f"Çarpma işleminin sonucu = {islem_sonucu}")
        elif secim == "4" :
            islem_sonucu = sayı1 / sayı2
            #print(f"Bölme işleminin sonucu = {islem_sonucu}")
        else :
            print("Yanlış seçim yaptınız, lütfen kontrol ediniz.!!!")
        # Çıktılar
        print(f"İşleminizin sonucu = {islem_sonucu}")
        # print("Program kapatılıyor")
    
    print()
    print("============================================")
    secim = input("Devam etmek istiyor musunuz ? (E/H) : ")
    if secim == "H" or secim == "h":
        print("Program kapatılıyor")
        print()
        break
