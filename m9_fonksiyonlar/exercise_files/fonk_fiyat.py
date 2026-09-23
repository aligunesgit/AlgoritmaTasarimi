"""M9 - Varsayılan parametre ve anahtar kelimeli argüman örnekleri."""


def kdvli_fiyat(fiyat: float, oran: float = 0.20) -> float:
    """KDV eklenmiş fiyatı kuruş hassasiyetinde (2 basamak) döndürür.

    oran verilmezse varsayılan olarak 0.20 (%20) kullanılır.
    """
    return round(fiyat * (1 + oran), 2)


def indirimli_fiyat(fiyat: float, yuzde: float = 10) -> float:
    """Fiyata yüzde cinsinden indirim uygular. yuzde=10 demek %10 indirim demektir."""
    return round(fiyat * (1 - yuzde / 100), 2)


def sepet_toplami(fiyatlar: list[float], indirim_yuzdesi: float = 0, kdv_orani: float = 0.20) -> float:
    """Sepetteki ürünlerin toplamına önce indirim, sonra KDV uygular.

    Hesabın her parçasını ayrı bir fonksiyona bırakır.
    """
    ara_toplam = 0.0
    for fiyat in fiyatlar:
        ara_toplam = ara_toplam + fiyat
    indirimli = indirimli_fiyat(ara_toplam, yuzde=indirim_yuzdesi)
    return kdvli_fiyat(indirimli, oran=kdv_orani)


if __name__ == "__main__":
    print(kdvli_fiyat(100))  # varsayılan oran: 120.0
    print(kdvli_fiyat(100, 0.10))  # konumsal argüman: 110.0
    print(kdvli_fiyat(oran=0.01, fiyat=100))  # anahtar kelimeli argüman: 101.0
    print(sepet_toplami([40, 60], indirim_yuzdesi=20))  # 96.0
