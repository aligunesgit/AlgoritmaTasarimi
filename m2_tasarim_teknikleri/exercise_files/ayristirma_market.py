"""M2 - Ayrıştırma: market fişinin toplamını küçük alt problemlerle hesaplamak.

Büyük problem ("fişin toplamını bul") dört küçük probleme ayrılmıştır. Her alt problem
ayrı bir fonksiyondur. Fonksiyonları M1'deki gibi, test edilebilsin diye bir kutuya
koyuyoruz; ayrıntısı M9'da.
"""


def ara_toplam(birim_fiyat: float, adet: int) -> float:
    """Alt problem 1: bir ürün satırının tutarı (fiyat × adet)."""
    return birim_fiyat * adet


def indirim_uygula(tutar: float, oran: float) -> float:
    """Alt problem 2: tutara indirim uygular. oran 0 ile 1 arasındadır (0.10 = %10)."""
    return tutar * (1 - oran)


def kdv_ekle(tutar: float, oran: float = 0.20) -> float:
    """Alt problem 3: tutara vergi ekler (örnek oran %20)."""
    return tutar * (1 + oran)


def fis_toplami(satir1: float, satir2: float, satir3: float, indirim_orani: float, kdv_orani: float = 0.20) -> float:
    """Alt problemleri birleştirir: satırları topla, indirim uygula, vergi ekle, kuruşa yuvarla."""
    toplam = satir1 + satir2 + satir3
    indirimli = indirim_uygula(toplam, indirim_orani)
    vergili = kdv_ekle(indirimli, kdv_orani)
    return round(vergili, 2)


if __name__ == "__main__":
    ekmek = ara_toplam(15.0, 2)
    sut = ara_toplam(42.5, 1)
    peynir = ara_toplam(90.0, 1)
    print(f"Fiş toplamı: {fis_toplami(ekmek, sut, peynir, 0.10)} TL")
