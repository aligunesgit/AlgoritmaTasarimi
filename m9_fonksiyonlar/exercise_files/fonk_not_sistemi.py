"""M9 - Büyük bir problemi fonksiyonlara bölmek: basit not sistemi."""


def ortalama_hesapla(notlar: list[float]) -> float:
    """Notların aritmetik ortalamasını döndürür. Liste boşsa 0.0 döndürür."""
    if len(notlar) == 0:
        return 0.0
    toplam = 0.0
    for not_degeri in notlar:
        toplam = toplam + not_degeri
    return toplam / len(notlar)


def harf_notu(ortalama: float) -> str:
    """0-100 arasındaki bir ortalamayı harf notuna çevirir.

    Ölçek örnektir; kendi üniversitenizin yönetmeliği farklı olabilir.
    """
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 80:
        return "BB"
    elif ortalama >= 75:
        return "CB"
    elif ortalama >= 70:
        return "CC"
    elif ortalama >= 60:
        return "DC"
    elif ortalama >= 50:
        return "DD"
    else:
        return "FF"


def rapor_yaz(ad: str, notlar: list[float]) -> str:
    """Öğrencinin adını, ortalamasını ve harf notunu içeren tek satırlık rapor döndürür.

    Kendi hesabını yapmaz; işi diğer iki fonksiyona devreder.
    """
    ort = ortalama_hesapla(notlar)
    harf = harf_notu(ort)
    return f"{ad}: ortalama {ort:.2f}, harf notu {harf}"


if __name__ == "__main__":
    ad = input("Öğrenci adı: ")
    adet = int(input("Kaç not gireceksiniz? "))
    notlar: list[float] = []
    for i in range(adet):
        notlar.append(float(input(f"{i + 1}. not: ")))
    print(rapor_yaz(ad, notlar))
