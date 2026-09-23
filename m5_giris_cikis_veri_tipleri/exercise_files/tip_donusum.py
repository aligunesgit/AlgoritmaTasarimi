"""M5 - Veri tipleri ve tip dönüşümü: metinden sayıya."""


def tip_adi(deger: object) -> str:
    """Bir değerin tipinin adını ("int", "float", "str", "bool") döndürür."""
    return type(deger).__name__


def yas_hesapla(dogum_yili_metni: str, bu_yil: int) -> int:
    """Metin olarak gelen doğum yılını tam sayıya çevirip yaşı döndürür.

    int() baştaki ve sondaki boşlukları kendisi atar. Metin bir tam sayı
    değilse (ör. "iki bin" ya da "2006.5") ValueError hatası fırlatır.
    """
    dogum_yili = int(dogum_yili_metni)
    return bu_yil - dogum_yili


if __name__ == "__main__":
    metin = input("Doğum yılınız: ")
    print("Girdiğiniz değerin tipi:", tip_adi(metin))
    print("Yaşınız (2026 itibarıyla):", yas_hesapla(metin, 2026))
