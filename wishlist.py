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

