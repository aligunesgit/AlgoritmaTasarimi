"""M4 - Aynı değişkenin değerinin adım adım değişmesi: kart bakiyesi."""


def son_bakiye(baslangic: float, yuklenen: float, harcanan: float) -> float:
    """Başlangıç bakiyesine yükleme yapılıp harcama düşüldükten sonraki bakiyeyi döndürür.

    Tek bir `bakiye` değişkeni üç kez değer alır. İz tablosunda bu değişkenin
    sütununda üç farklı satır, Python Tutor'da ise aynı kutunun değerinin
    değiştiğini görürsünüz.
    """
    bakiye = baslangic  # 1. başlangıç değeri
    bakiye = bakiye + yuklenen  # 2. yükleme
    bakiye = bakiye - harcanan  # 3. harcama
    return bakiye


if __name__ == "__main__":
    print("Son bakiye:", son_bakiye(40, 100, 17.5))
