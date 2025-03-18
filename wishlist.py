WISHLIST_FILE = "wishlist.txt"

def listeyi_goster():
    """İstek listesini ekrana yazdırır."""
    try:
        with open(WISHLIST_FILE, "r", encoding="utf-8") as file:
            wishlist = file.readlines()
            if not wishlist:
                print("İstek listeniz boş.")
            else:
                print("\n📜 İstek Listeniz:")
                for index, item in enumerate(wishlist, start=1):
                    print(f"{index}. {item.strip()}")
    except FileNotFoundError:
        print("Henüz bir wishlist oluşturulmadı.")

# Test için fonksiyonu çalıştır
listeyi_goster()


def istek_ekle():
    """Kullanıcıdan yeni bir istek alıp listeye ekler."""
    yeni_istek = input("Eklemek istediğiniz istek: ")
       with open(WISHLIST_FILE, "a", encoding="utf-8") as file:
        file.write(yeni_istek + "\n")
        print(f"'{yeni_istek}' istek listesine eklendi.")

def istek_sil():
    """Kullanıcının belirttiği numaradaki isteği siler."""
    listeyi_goster()  # Önce listeyi gösterelim
    try:
        silinecek = int(input("Silmek istediğiniz isteğin numarasını girin: ")) - 1
        with open(WISHLIST_FILE, "r", encoding="utf-8") as file:
            wishlist = file.readlines()

        if 0 <= silinecek < len(wishlist):
            silinen_istek = wishlist.pop(silinecek)
            with open(WISHLIST_FILE, "w", encoding="utf-8") as file:
                file.writelines(wishlist)
            print(f"🗑 '{silinen_istek.strip()}' istek listesinden silindi.")
        else:
            print("Geçersiz numara!")
    except (ValueError, FileNotFoundError):
        print("Hatalı giriş veya boş liste.")

# Test için fonksiyonu çalıştırabilirsin:
# istek_sil()       

# Test için fonksiyonu çalıştır (isteğe bağlı)
# istek_ekle()

# Ana menü
while True:
    print("\n🎯 Wishlist Uygulaması")
    print("1. Listeyi Göster")
    print("2. Yeni İstek Ekle")
    print("3. İstek Sil")
    print("4. Çıkış")

    secim = input("Seçiminizi yapın: ")
    
    if secim == "1":
        listeyi_goster()
    elif secim == "2":
        istek_ekle()
    elif secim == "3":
        istek_sil()
    elif secim == "4":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin!")