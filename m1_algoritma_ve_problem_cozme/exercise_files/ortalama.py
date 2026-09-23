"""M1 - İki sayının ortalaması (Pólya'nın dört adımına göre)."""


def ortalama(a: float, b: float) -> float:
    """İki sayının aritmetik ortalamasını döndürür."""
    toplam = a + b  # Adım 3: iki sayıyı topla
    return toplam / 2  # Adım 4: toplamı 2'ye böl


if __name__ == "__main__":
    birinci = float(input("Birinci sayı: "))  # Adım 1
    ikinci = float(input("İkinci sayı: "))  # Adım 2
    print(f"Ortalama: {ortalama(birinci, ikinci)}")  # Adım 5: sonucu göster
